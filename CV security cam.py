import cv2
import winsound
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret,frame1 = cam.read()
    ret,frame2 = cam.read()
    #taking absolute diff btw frame1 and frame2
    diff = cv2.absdiff(frame1,frame2)
    #cvt diff to gray
    gray = cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
    #blurring the image to reduce noise
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    #now we dilate the thresh
    dilated = cv2.dilate(thresh,None,iterations=4)
    contours,_= cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv2.contourArea(c)<5000:
            print("motion detected")
            continue
        x,y,w,h = cv2.boundingRect(c)
        #x,y are points w,h are width and hieght
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('security camera', frame1)
