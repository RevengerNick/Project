import cv2
print("Все работает!!!")

video = cv2.VideoCapture(0)

while True:
    good, img = video.read()
    img = cv2.resize(img, (720, 480))
    cv2.rectangle(img, (280, 300), (570, 390), (0, 150, 0), 2)
    cv2.putText(img, "LabRazum", (30, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 150), 2)
    cv2.imshow("Video", img)

    if cv2.waitKey(10) == ord('q'):
        break
