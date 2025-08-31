import cv2
scr = cv2.imread('./python_AI/day_3/image1.png')
gray = cv2.cvtColor(scr, cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(scr, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(scr, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(scr, cv2.COLOR_BGR2LAB)

cv2.imshow('scr', scr)
cv2.imshow('gray', gray)
cv2.imshow('rgb', rgb)
cv2.imshow('hsv', hsv)
cv2.imshow('lab', lab)

cv2.waitKey(0)
cv2.destroyAllWindows()