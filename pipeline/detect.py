from ultralytics import YOLO
import cv2

print("Loading model...")
model = YOLO("yolov8n.pt")

video_path = "videos/CAM 1.mp4"

print("Opening video...")
video = cv2.VideoCapture(video_path)

if not video.isOpened():
    print("Failed to open video")
    exit()

print("Video opened successfully")

ret, frame = video.read()

if not ret:
    print("Could not read frame")
    exit()

results = model(frame)

annotated = results[0].plot()

cv2.imwrite("test_detection.jpg", annotated)

print("Detection image saved as test_detection.jpg")

video.release()