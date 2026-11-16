import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

rotation = 0  # current rotation angle (0, 90, 180, 270)

while True:
    ret, frame = cap.read()
    

    # Apply rotation based on current state
    if rotation == 90:
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    elif rotation == 180:
        frame = cv2.rotate(frame, cv2.ROTATE_180)
    elif rotation == 270:
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

    cv2.imshow("Video", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):
        rotation = (rotation + 90) % 360   # rotate another 90°
    elif key == ord('q'):
        break

cap.release()

