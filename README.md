
#  ProDetect: Real-Time Smart Object Detection & Tracking

A professional-grade, modular object detection system built using YOLOv8, designed for real-time performance, zone-based alerts, and clean code structure.

---

##  Features

-  Real-time object detection (Webcam or Video)
-  Zone-based alerts for restricted areas
-  Modular architecture (easy to extend & maintain)
-  Save detections & log alerts to CSV
-  Optimized for GPU (GTX 1650 Ti or better)
-  YOLOv8 with optional BYTETracker
-  Live FPS & object count overlay

## 📂 Project Structure

```
prodetect/
├── models/                # Pretrained YOLOv8 model
├── utils/
│   ├── draw_utils.py      # Drawing boxes, labels
│   ├── zone_utils.py      # Restricted zone detection
├── detector.py            # YOLO detection + tracking
├── main.py                # Entry point
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation

1. **Clone the repo**  
```bash
git clone https://github.com/yourusername/prodetect.git
cd prodetect
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Download model**
```bash
# Place this in models/ directory
wget https://github.com/ultralytics/assets/releases/download/v8.0.0/yolov8n.pt -P models/
```

4. **Run the app**
```bash
python main.py
```

---

## 📦 Requirements

- Python 3.8+
- GPU (recommended)
- OpenCV
- Ultralytics (YOLOv8)
- Torch (with CUDA if possible)

---

## 📈 Output Example

- Red box = restricted zone
- Green box = detected object
- Logs get stored at `data/logs/detections.csv`

---

## 🔭 Future Ideas

- [ ] Stream to browser using Flask
- [ ] Object re-identification across cameras
- [ ] Crowd heatmaps
- [ ] Audio alerts / Telegram integration

---

## 📜 License

MIT License

---

## 🤝 Contributions

Pull requests are welcome! Let's build smarter AI surveillance together.
