#image filtering & noise removal
import cv2

img = cv2.imread("flowers.jpg")
gaussian = cv2.GaussianBlur(img, (5,5), 0)

median = cv2.medianBlur(img, 5)

average = cv2.blur(img, (5,5))

bilateral = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imwrite("gaussian.jpg", gaussian)
cv2.imwrite("median.jpg", median)
cv2.imwrite("average.jpg", average)
cv2.imwrite("bilateral.jpg", bilateral)

print("Filtering completed successfully!")
