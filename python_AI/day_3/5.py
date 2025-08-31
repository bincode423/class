import cv2
video = cv2.VideoCapture('./python_AI/day_3/img/video.mp4')
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        print("영상이 종료되었습니다.")
        break
    cv2.imshow('vedio', frame)
    if cv2.waitKey(25) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()