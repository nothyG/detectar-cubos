import imutils
import cv2
import pytesseract
import time
pytesseract.pytesseract.tesseract_cmd = r'D:\Programas\Tesseract-OCR\tesseract'
placa = []
cap = cv2.VideoCapture("MOV1.mp4")
while True:
  ret, frame = cap.read()
  frame = imutils.resize(frame,width=700)
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  gray = cv2.blur(gray,(3,3))

  ROI = frame[50:300,380:600]
  cv2.rectangle(frame,(380-2,50-2),(600+2,300+2),(255,0,0),1)
  grayROI = cv2.cvtColor(ROI,cv2.COLOR_BGR2GRAY)

  canny = cv2.Canny(gray,10,150)
  canny = cv2.dilate(canny,None,iterations=2)
  #_,cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
  cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
  #cv2.drawContours(frame,cnts,-1,(0,255,0),2)
  for c in cnts:
    area = cv2.contourArea(c)
    x,y,w,h = cv2.boundingRect(c)
    epsilon = 0.1*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,epsilon,True)
    if cv2.isContourConvex(c)==False :

      if len(approx)==4 and area>10000:
        cv2.drawContours(frame,[approx],0,(0,255,255),3)
        aspect_ratio = float(w)/h
        if aspect_ratio==1 and w==h:
          #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
          #cv2.drawContours(frame,[approx],0,(0,255,0),3)
          cv2.putText(frame, "Cubo",(x,y),1,2,(255,255,9),2)
          cv2.imshow("Encontrado",frame.copy())

      if len(approx)==5 and area>10000:
        #cv2.drawContours(frame,[approx],0,(255,0,255),3)
        aspect_ratio = float(w)/h
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        #cv2.drawContours(frame,[approx],0,(0,255,0),3)
        cv2.putText(frame, "Megaminx",(x,y),1,2,(255,255,9),2)
        cv2.imshow("Encontrado",frame.copy())

      if len(approx)==3 and area>10000:
        #cv2.drawContours(frame,[approx],0,(255,0,255),3)
        aspect_ratio = float(w)/h
        if aspect_ratio==1 and w==h:
          cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),3)
          cv2.drawContours(frame,[approx],0,(0,255,0),3)
          cv2.putText(frame, "Pyramix",(x,y),1,2,(255,255,9),2)
          cv2.imshow("Encontrado",frame.copy())
          time.sleep(2)
      
    #cv2.drawContours(frame, [approx], 0, (255,0,0))      
  cv2.imshow('frame',frame)
  cv2.imshow("Canny", canny)
  cv2.moveWindow('frame',45,10)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
# cv2.putText(frame,text,(x-20,y-10),1,2.2,(0,255,0),3)
cap.release()
cv2.destroyAllWindows()