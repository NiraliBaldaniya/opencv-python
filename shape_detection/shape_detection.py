import cv2


image_path = input("Enter image path: ")
image = cv2.imread(image_path) 

if image is None:
    print("Image not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0,255,0), 2)

for contour in contours:
    
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    corners = len(approx)

    if corners == 3:
        shape_name = "Triangle"

    elif corners == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)

        if 0.95 <= aspect_ratio <= 1.05:
            shape_name = "Square"
        else:
            shape_name = "Rectangle"
    
    elif corners == 5:
        shape_name = "Pentagon"

    elif corners > 5:
        shape_name = "Circle"
    else:
        shape_name = "unknown shape"

    cv2.drawContours(image, [approx], 0, (0, 0, 255), 2)

    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    cv2.putText(image, shape_name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

cv2.imshow("Original Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()