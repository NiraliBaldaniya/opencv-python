import cv2
import numpy as np

image = cv2.imread("blue_image.png")

if image is None:
    print("Image not found!")
else:
    sharp_kernel = np.array([
            [-1,-1,-1],
            [-1,9,-1],
            [-1,-1,-1]
    ])

    sharp_image = cv2.filter2D(image, -1, sharp_kernel)

    cv2.imshow("Original Image", image)
    cv2.imshow("Sharpened Image", sharp_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
