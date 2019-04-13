#Importing libraries
import numpy as np
import cv2

def compare():         #loading of the images
    img = cv2.imread('gsp.png',255)  
    img1 = cv2.imread('gs.jpg', 255)   #Comparing the shape in terms of pixel and size

    pica = img.shape   #gives the pixels of img
    picb = img1.shape  #give the pixels of img1
    print(pica)
    print(picb)
    
    if pica == picb:
        print("The images have same size and channels")
    else: 
        print("The images are unequal");
    
            
    cv2.imshow('image',img)
    cv2.imshow('image',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    

compare()

