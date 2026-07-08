import cv2

image = cv2.imread("blur_image.png")

if image is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh_image = cv2.threshold(gray, 105, 255, cv2.THRESH_BINARY)

    cv2.imshow("Original Image", image)
    cv2.imshow("Threshold Image", thresh_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()