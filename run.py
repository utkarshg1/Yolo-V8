from ultralytics import YOLO

model = YOLO("yolov8x.pt")

model("images/basketball.jpg")