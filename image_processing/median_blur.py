import cv2

image = cv2.imread("blur_image.png")

if image is None:
    print("Image not found!")
else:
    median_blur = cv2.medianBlur(image, 11)

    cv2.imshow("Original Image", image)
    cv2.imshow("Median Blur", median_blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()