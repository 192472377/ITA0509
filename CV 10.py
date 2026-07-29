import cv2

# ✅ Update with your actual image path
image_path = r"C:\Users\gandl\Downloads\download (1).jpeg"

# Read the image
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not read the image. Check the path and filename.")
else:
    # --- Method 1: Rotate 90 degrees clockwise ---
    rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # --- Method 2: Flip horizontally (simulate y-axis rotation) ---
    flipped = cv2.flip(image, 1)  # 1 = horizontal flip

    # Display results
    cv2.imshow("Original Image", image)
    cv2.imshow("90 Degree Clockwise Rotation", rotated)
    cv2.imshow("Y-axis Flip (Horizontal)", flipped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
