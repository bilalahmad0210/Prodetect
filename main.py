import cv2
import time
import torch
from detector import Detector
from utils.draw_utils import draw_boxes
from utils.zone_utils import draw_zone, check_violation
from utils.logger import log_detection

def main():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)   # Lower resolution for speed
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    detector = Detector(model_path='models/yolov8n.pt', use_cuda=True)  # Light model for better FPS

    frame_count = 0
    show_zone = True  # Toggle zone overlay (set False to remove red box)

    while True:
        start_time = time.time()
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        # Run detection
        results = detector.detect(frame)

        # Draw restricted zone
        if show_zone:
            draw_zone(frame)

        # Draw detections
        frame = draw_boxes(frame, results, detector.names)

        # Check zone violations
        if results and results.boxes:
            for box in results.boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                if check_violation(box):
                    log_detection(detector.names[cls], conf)

        # Calculate and display FPS
        fps = 1.0 / (time.time() - start_time + 1e-5)
        cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

        # Show frame
        cv2.imshow("ProDetect: Real-Time Object Detection", frame)

        # Exit condition
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
