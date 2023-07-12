import cv2
from source_code.object_detection import ObjectDetection

cap = cv2.VideoCapture('rtsp://flussonic2.powernet.com.ru/user72349')
od = ObjectDetection()

while True:
    _, frame = cap.read()

    class_ids, scores, boxes = od.detect(frame)
    count_boxes = 0
    for box in boxes:
        x, y, z, w = box
        cv2.rectangle(frame, (x, y), (x+z, y+w), (255, 0, 0), 2)
        count_boxes += 1
    print(f'Кол-во авто : {count_boxes}')
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
