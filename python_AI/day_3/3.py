import cv2
 
img = cv2.imread('./python_AI/day_3/img/image1.png', cv2.IMREAD_COLOR)
 
cartoon_img = cv2.stylization(img, sigma_s=100, sigma_r=0.9)  
 
cv2.imshow('original', img)
cv2.imshow('cartoon', cartoon_img)  
cv2.waitKey(0)  
cv2.destroyAllWindows() 
 
cv2.imwrite('./python_AI/day_3/img/img2_cartoon.jpg', cartoon_img)