import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = r"C:\Users\gandl\Downloads\download (1).jpeg"
image = cv2.imread(image_path)

# Get image dimensions
rows, cols, ch = image.shape

# Define 4 points in the original image (source points)
pts1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])

# Define 4 points in the output image (destination points)
pts2 = np.float32([[10, 100], [200, 50], [100, 250], [250, 250]])

# Compute the Perspective Transformation matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Apply the transformation
perspective_transformed = cv2.warpPerspective(image, M, (cols, rows))

# Convert BGR to RGB for Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
perspective_rgb = cv2.cvtColor(perspective_transformed, cv2.COLOR_BGR2RGB)

# Display original and transformed images side by side
plt.figure(figsize=(10,5))

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(perspective_rgb)
plt.title("Perspective Transformed Image")
plt.axis("off")

plt.show()
