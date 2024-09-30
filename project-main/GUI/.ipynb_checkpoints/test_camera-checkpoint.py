import cv2

def test_camera(camera_index=0):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"Error: Unable to open camera with index {camera_index}.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Camera Test', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    for index in range(5):  # 최대 5개의 카메라 인덱스를 시도
        print(f"Testing camera with index {index}")
        test_camera(index)
