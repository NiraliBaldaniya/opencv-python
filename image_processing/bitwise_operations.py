import cv2
import numpy as np

img1= np.zeros((300,300),dtype="uint8")
img2= np.zeros((300,300),dtype="uint8")

cv2.circle(img1,(150,150),100,255,-1)
cv2.rectangle(img2,(100,100),(250,250),255,-1)

bitwise_and = cv2.bitwise_and(img1,img2)
bitwise_or = cv2.bitwise_or(img1,img2)
bitwise_xor =cv2.bitwise_xor(img1,img2)

cv2.imshow("Original Image 1", img1)
cv2.imshow("Original Image 2", img2)
cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise XOR", bitwise_xor)
cv2.waitKey(0)
cv2.destroyAllWindows()