import cv2
import numpy as np

# ✅ Update this path to match your actual image file
image_path = r"C:\Users\gandl\Downloads\download (1).jpeg"

# Read the image
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not read the image. Check the path and filename.")
else:
    # Create a kernel (structuring element)
    kernel = np.ones((5, 5), np.uint8)

    # Perform dilation
    dilated_image = cv2.dilate(image, kernel, iterations=1)

    # Display original and dilated images
    cv2.imshow("Original Image", image)
    cv2.imshow("Dilated Image", dilated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
