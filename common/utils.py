import json
import cv2

def load_config(path="config/default.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def in_roi(box, roi):
    x1,y1,x2,y2 = box
    rx1,ry1 = roi[0]
    rx2,ry2 = roi[1]
    cx = (x1+x2)//2
    cy = (y1+y2)//2
    return rx1<cx<rx2 and ry1<cy<ry2

def cross_two_lines(track, line1, line2):
    return False