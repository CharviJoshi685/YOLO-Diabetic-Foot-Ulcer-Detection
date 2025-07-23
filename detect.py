# detect.py
# Launch this from inside the yolov5 directory or adjust paths if outside

import os

# Example detection command
os.system("""
python detect.py \
  --weights ../runs/yolo-dfu/weights/best.pt \
  --img 640 \
  --conf 0.25 \
  --source ../data/test
""")
