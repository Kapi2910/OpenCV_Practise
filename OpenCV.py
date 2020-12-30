import cv2
import numpy as npy
import matplotlib.pyplot as plt

img_CV = cv2.imread('images/ManCity_Logo.png')


b, g, r = cv2.split(img_CV)

img_plt = cv2.merge([r, g, b])

def ImageByPlt(img_CV, img_plt):
    plt.subplot(121)
    plt.imshow(img_CV)
    plt.subplot(122)
    plt.imshow(img_plt)
    plt.show()

def ImageByCV(img_CV, img_plt):
    img_concate = npy.concatenate((img_CV, img_plt), axis=1)
    cv2.imshow( "BGR", img_CV)    
    cv2.imshow( "RGB", img_plt)    
    cv2.imshow( "BGR & RGB", img_concate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



ImageByCV(img_CV, img_plt)    
