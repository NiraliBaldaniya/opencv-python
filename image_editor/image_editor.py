import cv2

def resize():
        w = int(input("enter image width: "))
        h = int(input("enter image height: "))

        resized_image = image.copy()
        resized_image = cv2.resize(resized_image,(w,h))

        output(resized_image, "Resized Image")
def rotate():
        rotated_image = image.copy()
        (h,w) = rotated_image.shape[:2]
        center = (w//2 , h//2)
        angle = int(input("enter your image angle: "))

        scale=float(input("Enter the font scale {1.0 : Normal , 2.0 : large ,0.5 : small}: "))

        m = cv2.getRotationMatrix2D(center,angle,scale)
        rotated_image = cv2.warpAffine(rotated_image,m,(w,h))
        output(rotated_image, "Rotated Image")
   

def draw_line():
        x1 = int(input("enter x1 point: "))
        y1 = int(input("enter y1 point: "))
        pt1 = (x1,y1)
        x2 = int(input("enter x2 point: "))
        y2 = int(input("enter y2 point: "))
        pt2 = (x2,y2)
        r=int(input("Enter the value of red (0-255): ")) 
        g=int(input("Enter the value of green (0-255): ")) 
        b=int(input("Enter the value of blue (0-255): ")) 
        color=(b,g,r) 
        thickness=int(input("Enter the thickness of the line: ")) 

        line_image = image.copy()
        cv2.line(line_image,pt1,pt2,color,thickness) 
        output(line_image, "Line Image")


def draw_rectangle():
        x1 = int(input("enter x1 point: "))
        y1 = int(input("enter y1 point: "))
        pt1 = (x1,y1)
        x2 = int(input("enter x2 point: "))
        y2 = int(input("enter y2 point: "))
        pt2 = (x2,y2)

        r=int(input("Enter the value of red (0-255): ")) 
        g=int(input("Enter the value of green (0-255): ")) 
        b=int(input("Enter the value of blue (0-255): ")) 
        color=(b,g,r) 
        thickness=int(input("Enter the thickness of the line: ")) 

        rectangle_image = image.copy()
        cv2.rectangle(rectangle_image,pt1,pt2,color,thickness) 
        output(rectangle_image, "Rectangle Image")
    

def draw_circle():
        x = int(input("enter center x point: "))
        y = int(input("enter center y point: "))
        center = (x,y)
        radius = int(input("enter radius: "))


        r=int(input("Enter the value of red (0-255): ")) 
        g=int(input("Enter the value of green (0-255): ")) 
        b=int(input("Enter the value of blue (0-255): ")) 
        color=(b,g,r) 
        thickness=int(input("Enter the thickness of the line: ")) 

        circle_image = image.copy()
        cv2.circle(circle_image,center,radius,color,thickness)

        output(circle_image, "Circle Image")

def add_text():
        text = input("enter text that you want to add: ")


        x = int(input("enter  x point: "))
        y = int(input("enter  y point: "))
        point = (x,y)

        fontface=cv2.FONT_HERSHEY_COMPLEX 
        fontscale=float(input("Enter the font scale {1.0 : Normal , 2.0 : large ,0.5 : small}: "))

        r=int(input("Enter the value of red (0-255): ")) 
        g=int(input("Enter the value of green (0-255): ")) 
        b=int(input("Enter the value of blue (0-255): ")) 
        color=(b,g,r) 
        thickness=int(input("Enter the thickness of the line: ")) 
        text_image = image.copy()
        cv2.putText(text_image,text,point,fontface,fontscale,color,thickness)

        output(text_image, "Text Image")
def grayscale():
        grayscaleimage= image.copy()
        grayscaleimage = cv2.cvtColor(grayscaleimage,cv2.COLOR_BGR2GRAY)

        output(grayscaleimage, "Grayscale Image")


def output(image, window_name):
        print("1. Show Image")
        print("2. Save Image")

        choice = int(input("Enter choice: "))

        if choice == 1:
            cv2.imshow(window_name, image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif choice == 2:
            filename = input("Enter output file name: ")
            cv2.imwrite(f"{filename}.jpg", image)

        else:
            print("Invalid choice")

file__name = input("enter your image location: ")
image = cv2.imread(file__name)
if image is not None:
    print("choose your options")
    while True:
        print("1. Draw Line")
        print("2. Draw Rectangle")
        print("3. Draw Circle")
        print("4. Add Text")
        print("5. Convert to Grayscale")
        print("6. Resize Image")
        print("7. Rotate Image")
        print("8. Exit")
        option = int(input("enter your chosen number: "))

        if option == 1:
            draw_line()

        elif option==2: 
            draw_rectangle()

        elif option == 3:
            draw_circle()

        elif option == 4:
            add_text()

        elif option == 5:
            grayscale()

        elif option == 6:
             resize()

        elif option == 7:
             rotate()

        elif option == 8:
            print("exit complete")
            break
        else:
            print("invalid option")
else:
    print("image not found")
    


