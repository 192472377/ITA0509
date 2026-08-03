import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = r"C:\Users\gandl\Downloads\download (1).jpeg"
image = cv2.imread(image_path)

# Get image dimensions
rows, cols, ch = image.shape

# Define 3 points in the original image
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

# Define where those points should map to in the transformed image
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Compute the Affine Transformation matrix
M = cv2.getAffineTransform(pts1, pts2)

# Apply the transformation
affine_transformed = cv2.warpAffine(image, M, (cols, rows))

# Convert BGR to RGB for Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
affine_rgb = cv2.cvtColor(affine_transformed, cv2.COLOR_BGR2RGB)

# Display original and transformed images side by side
plt.figure(figsize=(10,5))

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(affine_rgb)
plt.title("Affine Transformed Image")
plt.axis("off")

plt.show()
