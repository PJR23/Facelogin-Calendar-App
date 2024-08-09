import face_recognition
import cv2
import sys

def main():
    try:
        video_capture = cv2.VideoCapture(0)
        if not video_capture.isOpened():
            print("Error: Camera is not available.")
            return
    except Exception as e:
        print(f"An error occurred while opening the video source: {e}")
        return

    last_face_landmarks_list = []

    try:
        while True:
            ret, frame = video_capture.read()
            if not ret:
                print("Error: Can't receive frame (stream end?). Exiting ...")
                break

            rgb_frame = frame[:, :, ::-1]

            try:
                face_landmarks_list = face_recognition.face_landmarks(rgb_frame)
            except Exception as e:
                print(f"Error in face recognition: {e}")
                face_landmarks_list = last_face_landmarks_list

            if not face_landmarks_list and last_face_landmarks_list:
                face_landmarks_list = last_face_landmarks_list
            else:
                last_face_landmarks_list = face_landmarks_list

            for face_landmarks in face_landmarks_list:
                for facial_feature in face_landmarks:
                    points = face_landmarks[facial_feature]
                    for point in points:
                        cv2.circle(frame, point, 2, (0, 255, 0), -1)

            cv2.imshow('Video - Press Q to quit', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
