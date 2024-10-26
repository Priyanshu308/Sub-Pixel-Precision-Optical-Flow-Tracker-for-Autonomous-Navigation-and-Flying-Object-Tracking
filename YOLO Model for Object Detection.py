import torch

def detect_objects(frame, model):
    results = model(frame)
    boxes = results.xyxy[0]  # Bounding boxes for detected objects
    return boxes
