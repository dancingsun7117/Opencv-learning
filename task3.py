import cv2

frame = None

cap = cv2.VideoCapture(1)

def mouse_event(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN and frame is not None:

        print(f"Pixel Coordinates: x={x}, y={y}")

        b, g, r = frame[y, x]

        print(f"Color (BGR): {b}, {g}, {r}")

cv2.namedWindow('Live Video')
cv2.setMouseCallback('Live Video', mouse_event)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('Live Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()