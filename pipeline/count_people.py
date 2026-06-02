from ultralytics import YOLO
import cv2
import json

print("Loading YOLO model...")
model = YOLO("yolov8n.pt")

videos = [
    "videos/CAM 1.mp4",
    "videos/CAM 2.mp4",
    "videos/CAM 3.mp4",
    "videos/CAM 4.mp4",
    "videos/CAM 5.mp4"
]

results_summary = {}

for video_path in videos:

    print(f"\nProcessing {video_path}")

    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)

    frame_skip = int(fps * 5)

    frame_count = 0

    people_counts = []

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        if frame_count % frame_skip == 0:

            results = model(frame, verbose=False)

            people = 0

            for box in results[0].boxes:

                cls = int(box.cls[0])

                if cls == 0:
                    people += 1

            people_counts.append(people)

        frame_count += 1

    cap.release()

    if len(people_counts) > 0:

        max_people = max(people_counts)

        avg_people = round(
            sum(people_counts) / len(people_counts),
            2
        )

    else:

        max_people = 0
        avg_people = 0

    camera_name = video_path.split("/")[-1]

    results_summary[camera_name] = {
        "max_people": max_people,
        "average_people": avg_people,
        "samples_processed": len(people_counts)
    }

print("\n===== FINAL SUMMARY =====")

for camera, stats in results_summary.items():

    print(camera)

    print("Max People:", stats["max_people"])

    print("Average People:", stats["average_people"])

    print("Samples:", stats["samples_processed"])

    print()

with open(
    "data/cctv_summary.json",
    "w"
) as f:

    json.dump(
        results_summary,
        f,
        indent=4
    )

print("Saved -> data/cctv_summary.json")