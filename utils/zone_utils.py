import numpy as np
import cv2

RESTRICTED_ZONE = [(100,100), (500,100), (500,500), (100,500)]

def draw_zone(frame):
    cv2.polylines(frame, [np.array(RESTRICTED_ZONE)], isClosed=True, color=(0,0,255), thickness=2)

def check_violation(box):
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
    return cv2.pointPolygonTest(np.array(RESTRICTED_ZONE), (cx, cy), False) >= 0
