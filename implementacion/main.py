from similaritymeasures import Similarity
import cv2
import numpy as np

def compare(x,y,option):
    # comparer
    sm = Similarity()

    c1 = 0, 0
    
    if option == 1:        
        c1 = sm.euclidean_distance(x, y)
    elif option==2:
        c1 = sm.manhattan_distance(x, y)
    elif option==3:
        c1 = sm.minkowski_distance(x, y, 3)        
    elif option==4:        
        c1 = sm.cosine_similarity(x, y)        
    elif option==5:
        c1 = sm.jaccard_similarity(x, y)
    else:
        c1 = -1     
    
    return c1


def main():        
    #1 image
    image_1 = cv2.imread('img/manzana_1.jpg') 
    gray_image = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY) 
    histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256]) 
    
    # 2 image 
    image_2 = cv2.imread('img/manzana_2.jpg') 
    gray_image1 = cv2.cvtColor(image_2, cv2.COLOR_BGR2GRAY) 
    histogram1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256]) 
    
    # test 3 image 
    image_3 = cv2.imread('img/manzana_3.jpg') 
    gray_image2 = cv2.cvtColor(image_3, cv2.COLOR_BGR2GRAY) 
    histogram2 = cv2.calcHist([gray_image2], [0], None, [256], [0, 256]) 

    c1, c2 = 0, 0
   
    #Distance 
    #opcion 1: euclidean
    #c1 = compare(histogram, histogram2, 1)
    #c2 = compare(histogram1, histogram2, 1) 
    #opcion 2: manhattan
    c1 = compare(histogram, histogram2, 2)
    c2 = compare(histogram1, histogram2, 2) 
    #opcion 3: minkowski
    #c1 = compare(histogram, histogram2, 3)
    #c2 = compare(histogram1, histogram2, 3) 
    #opcion 4: cosine
    #c1 = compare(histogram, histogram2, 4)
    #c2 = compare(histogram1, histogram2, 4) 
    #opcion 5: jaccard
    #c1 = compare(histogram, histogram2, 5)
    #c2 = compare(histogram1, histogram2, 5)        
    
    if(c1<c2): 
        print("Imagen 1 is more similar to test image as compare to imagen 2") 
    else: 
        print("Imagen 2 is more similar to test image as compare to imagen 1")
    
    cv2.imshow("Original 1", image_1)
    cv2.imshow("Original 2", image_2)
    cv2.imshow("Prueba", image_3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main() 