import cv2

video = cv2.VideoCapture(0)

while video.isOpened():
    ret, frame = video.read()
    cartoon_img = cv2.stylization(frame, sigma_s=100, sigma_r=1)  
    cv2.imshow('cartoon', cartoon_img)
    if cv2.waitKey(25) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()