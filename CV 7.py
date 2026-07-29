import cv2

def play_video(video_path, speed=1):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000 / (fps * speed))  # Adjust delay based on speed

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Video Playback", frame)

        # Press 'q' to quit
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# ✅ Use raw string for Windows paths to avoid errors
video_path = r"C:\Users\gandl\Downloads\vlipsy-tom-and-jerry-happy-birthday-ohU7gs2i.mp4"

# Normal speed
print("Playing video at normal speed...")
play_video(video_path, speed=1)

# Slow motion (0.5x speed)
print("Playing video in slow motion...")
play_video(video_path, speed=0.5)

# Fast motion (2x speed)
print("Playing video in fast motion...")
play_video(video_path, speed=2)
