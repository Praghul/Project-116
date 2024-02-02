import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Solar System", (500,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0))

cv2.putText(img,"Sun", (90,400), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))

cv2.putText(img,"Mercury", (110,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putText(img,"Venus", (190,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putText(img,"Earth", (280,260), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putText(img,"Mars", (380,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putText(img,"Jupiter", (540,380), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putText(img,"Saturn", (750,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putText(img,"Uranus", (970,290), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putText(img,"Neptune", (1110,290), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.imshow("output", img)
cv2.waitKey(10000)

