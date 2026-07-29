import cv2
import numpy as np
image = cv2.imread(r"C:\Users\gandl\OneDrive\Pictures\79bf9007bdf1c0372485db0c4f226621.jpg") # Replace with your image file
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized_image = cv2.equalizeHist(gray_image)
cv2.imshow("Original Grayscale Image", gray_image)
cv2.imshow("Histogram Equalized Image", equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
