import cv2
image = cv2.imread("solar-system.jpg")
cv2.putText(image,"sun",(100,80),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(image,"mercury",(110,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(image,"venus",(190,270),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(image,"earth",(300,270),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(image,"mars",(400,270),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(image,"jupiter",(500,90),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(image,"saturn",(720,110),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(image,"uranus",(950,130),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(image,"neptune",(1080,130),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.imshow("output",image)
cv2.waitKey(0)
cv2.imwrite("solar_system_with_name.jpg",image)