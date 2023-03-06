import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"sun",(20,110),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=1,color=(0,0,250))
cv2.putText(img,"Mercury",(105,200),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(0,0,250))
cv2.putText(img,"Venus",(200,205),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(0,0,250))
cv2.putText(img,"Earth",(300,200),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(0,0,250))
cv2.putText(img,"Mars",(400,205),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(0,0,250))
cv2.putText(img,"Jupiter",(550,325),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(0,0,250))
cv2.putText(img,"Saturn",(750,205),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(0,0,250))
cv2.putText(img,"Uranus",(1000,250),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(0,0,250))
cv2.putText(img,"Neptune",(1100,230),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(0,0,250))

cv2.imshow("output",img)
cv2.waitKey(0)