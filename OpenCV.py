import cv2

img = cv2.imread('images/logo.png')

dimensions = img.shape  
size = img.size         # size = height * width * channels
img_type = img.dtype

(b, r, g) = img[0, 0]

print(
    f"Dimensions:{dimensions}\n",
    f"Blue:{b}",
    f"Green:{g}",
    f"Red:{r}"
)


cv2.imshow("Image", img)
cv2.waitKey(0)