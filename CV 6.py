import cv2
image = cv2.imread(r"C:\Users\gandl\OneDrive\Pictures\79bf9007bdf1c0372485db0c4f226621.jpg") # Replace 'sample.jpg' with your image path
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
