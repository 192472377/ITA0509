import cv2
import numpy as np

# Read the image
image_path = r"C:\Users\gandl\Downloads\download (1).jpeg"
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Harris Corner Detection
dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Dilate for better visibility
dst = cv2.dilate(dst, None)

# Mark corners in red
image[dst > 0.01 * dst.max()] = [0, 0, 255]

# Show input and output in OpenCV windows
cv2.imshow("Original Image", cv2.imread(image_path))
cv2.imshow("Corners Detected", image)

cv2.waitKey(0)   # Wait until a key is pressed
cv2.destroyAllWindows()

