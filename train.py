# train.py
# Launch this from inside the yolov5 directory after cloning Ultralytics' repo

import os

# Example training command
os.system("""
python train.py \
  --img 640 \
  --batch 16 \
  --epochs 50 \
  --data ../data/dfu.yaml \
  --weights yolov5s.pt \
  --project ../runs \
  --name yolo-dfu
""")
