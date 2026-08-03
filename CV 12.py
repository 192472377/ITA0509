import cv2
import matplotlib.pyplot as plt

# Load the image
image_path = r"C:\Users\gandl\Downloads\download (1).jpeg"
image = cv2.imread(image_path)

# Step 1: Flip horizontally (y-axis rotation)
flipped = cv2.flip(image, 1)

# Step 2: Rotate 270° clockwise
rotated_270 = cv2.rotate(flipped, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Convert BGR to RGB for Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
rotated_rgb = cv2.cvtColor(rotated_270, cv2.COLOR_BGR2RGB)

# Display both images side by side
plt.figure(figsize=(10,5))

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(rotated_rgb)
plt.title("270° Clockwise (y-axis)")
plt.axis("off")

plt.show()
