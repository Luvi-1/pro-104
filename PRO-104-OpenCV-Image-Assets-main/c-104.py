import cv2

img = cv2.imread('poster.jpg')
rocketimg = img[120:360,400:500]
img[0:240,500:600] = rocketimg
cv2.putText(img,"Hi how are you?",(20,110),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=1,color=(0,0,250))
cv2.imshow('output', img)
cv2.waitKey(0)