import cv2
import time
import os
wcam , hcam = 640,480
cap = cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
folderPath = "Hands"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for impath in myList:
    image = cv2.imread(folderPath + '/' + impath)
    overlayList.append(image)
    
print(len(overlayList))
while True:
    success, img = cap.read()
    h,w,c = overlayList[0].shape
    img[0:h,0:w] = overlayList[0]
    pTime = 0
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    #cv2.putText(img, "FPS: " + fps, (400,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
