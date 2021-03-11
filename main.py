import cv2
import numpy as np
import pytesseract
import os


#percentage accuracy
per = 35


#reading the query image, which is my template
imgQ = cv2.imread("template.png")
h,w,c = imgQ.shape
imgQ = cv2.resize(imgQ, (w//2, h//2))


#using the orb to detect keypoints
orb = cv2.ORB_create(5000)
kp1, des1 = orb.detectAndCompute(imgQ, None)

img = cv2.imread("test1.jpg")
kp2, des2 = orb.detectAndCompute(img, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING)

#imgKp1 = cv2.drawKeypoints(imgQ, kp1, None)
#cv2.imshow("kp1",imgKp1 )


matches = bf.match(des2, des1)
matches.sort(key = lambda x: x.distance)
good = matches[:int(len(matches)*(per/100))]
imgMatch = cv2.drawMatches(img, kp2, imgQ, kp1, good, None, flags=2)
imgMatch = cv2.resize(imgMatch, (w//2, h//2))
cv2.imshow("test", imgMatch)

srcPoints = np.float32([kp2[m.queryIdx].pt for m in good]).reshape(-1,1,2)
dstPoints = np.float32([kp1[m.trainIdx].pt for m in good]).reshape(-1,1,2)

M, _ = cv2.findHomography(srcPoints, dstPoints, cv2.RANSAC, 5.0)
imgScan = cv2.warpPerspective(img, M, (w,h))
cv2.imshow("final", imgScan)

#cv2.imshow("template", imgQ)
cv2.waitKey(0)
