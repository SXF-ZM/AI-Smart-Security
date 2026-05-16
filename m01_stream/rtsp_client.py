import cv2
import threading

class RTSPStream:
    def __init__(self, url="rtsp://192.168.1.100:554/stream"):
        self.url = url
        self.cap = None
        self.running = False
        self.current_frame = None

    def start(self):
        self.running = True
        self.cap = cv2.VideoCapture(self.url)
        threading.Thread(target=self._read, daemon=True).start()

    def _read(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                self.reconnect()
                continue
            self.current_frame = frame

    def reconnect(self):
        self.cap.release()
        self.cap = cv2.VideoCapture(self.url)