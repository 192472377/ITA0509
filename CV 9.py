import cv2

# ✅ Use raw string for Windows paths to avoid errors
image_path = r"C:\Users\gandl\Downloads\download (1).jpeg"

# Read the image
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not read the image. Check the path and filename.")
else:
    # Get original dimensions
    height, width = image.shape[:2]
    print(f"Original Size: {width}x{height}")

    # Resize to half (smaller)
    smaller = cv2.resize(image, (width // 2, height // 2), interpolation=cv2.INTER_AREA)

    # Resize to double (bigger)
    bigger = cv2.resize(image, (width * 2, height * 2), interpolation=cv2.INTER_CUBIC)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Smaller Image", smaller)
    cv2.imshow("Bigger Image", bigger)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
