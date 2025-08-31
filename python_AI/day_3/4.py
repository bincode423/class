import cv2

img = cv2.imread('./python_AI/day_3/img/image1.png', cv2.IMREAD_COLOR)

gray_sketch, color_sketch = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.0)

cv2.imshow('Original', img)
#cv2.imshow('Pencil Sketch (Gray)', gray_sketch)
cv2.imshow('Pencil Sketch (Color)', color_sketch)

#cv2.imwrite('./python_AI/day_3/img/img2_pencil_gray.jpg', gray_sketch)
#cv2.imwrite('./python_AI/day_3/img/img2_pencil_color.jpg', color_sketch)

cv2.waitKey(0)
cv2.destroyAllWindows()