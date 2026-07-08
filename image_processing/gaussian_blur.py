import cv2

image = cv2.imread("blur_image.png")

if image is None:
    print("Image not found!")
else:
    blurred_image = cv2.GaussianBlur(image, (31, 31), 0)

    cv2.imshow("Original Image", image)
    cv2.imshow("Gaussian Blur", blurred_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()