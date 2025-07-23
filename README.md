# YOLO-Based Diabetic Foot Ulcer Detection 🦶

A real-time object detection project to identify diabetic foot ulcers (DFU) in clinical images using YOLOv5.

## 🧠 Objective
To automate early screening of diabetic foot ulcers and assist clinical diagnosis using deep learning.

## 🧪 Dataset
- [Kaggle DFU Dataset](https://www.kaggle.com/datasets/laithjj/diabetic-foot-ulcer-dfu)
- [DFUC2020 Challenge](https://dfu2020.grand-challenge.org/) (request access)

## 🚀 Getting Started

```bash
git clone https://github.com/YOUR_USERNAME/YOLO-Diabetic-Foot-Ulcer-Detection.git
cd YOLO-Diabetic-Foot-Ulcer-Detection
pip install -r requirements.txt
```

## 🏋️‍♀️ Training

```bash
cd yolov5
python train.py --img 640 --batch 16 --epochs 50 --data ../data/dfu.yaml --weights yolov5s.pt
```

## 🔍 Inference

```bash
python detect.py --weights runs/train/exp/weights/best.pt --source ../data/test
```

## 💡 Sample Result
Detection results are saved in `runs/detect/exp`.

## 🤝 Acknowledgments
Based on Ultralytics YOLOv5. Dataset from DFUC2020 & Kaggle.
