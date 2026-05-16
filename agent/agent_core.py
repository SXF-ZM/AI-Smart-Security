import time
import json
from m01_stream.rtsp_client import RTSPStream
from m02_detect.detector import SmartDetector
from m02_detect.rules import fire_channel_occupy, car_retention, person_retention
from m03_signal.emqx_client import EMQXClient
from m05_config.redis_config import get_config

class Agent:
    def __init__(self, rtsp_url):
        self.stream = RTSPStream(rtsp_url)
        self.detector = SmartDetector()
        self.emqx = EMQXClient()
        self.cfg = get_config()
        self.timers = {}

    def run(self):
        self.stream.start()
        print("Agent启动成功，开始检测...")
        while True:
            frame = self.stream.current_frame
            if frame is None:
                time.sleep(0.01)
                continue
            boxes, confs, clss = self.detector.detect(frame)
            tracks = self.detector.track(frame, boxes, confs)
            self.judge_and_send(boxes, tracks)
            time.sleep(0.03)

    def judge_and_send(self, boxes, tracks):
        now = time.time()
        # F01 消防通道占用
        f01 = fire_channel_occupy(boxes, self.cfg["roi_fire"], 300)
        # F02 车辆滞留
        f02 = car_retention(boxes, self.cfg["roi_fire"], 180)
        # F04 人员滞留
        f04 = person_retention(tracks, self.cfg["roi_fence"], 120)

        sig = {
            "detection_type": "fire_channel_occupy",
            "area_id": "fire_001",
            "detect_time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "is_abnormal": f01,
            "target_count": len(boxes)
        }
        self.emqx.publish("detect/signals", sig)