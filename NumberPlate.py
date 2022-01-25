import  cv2
frameWidth = 840
frameHieght = 480
cap = cv2.VideoCapture(1)

nPlatesCascade = cv2.CascadeClassifier("Number_Plate.xml")
cap.set(3,frameWidth)
cap.set(4 , frameHieght)
cap.set(10,150)
count = 0

while True:
    success ,img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlatesCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in numberPlates:

        area = w*h
        if area>500:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 225, 0), 2)
            cv2.putText(img , "Number Plate" ,(x , y - 5) ,cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,255) ,2)
            imgRoi = img[y:y+h , x:x+w]
            cv2.imshow("ROI" , imgRoi)

    cv2.imshow("Result" , img)


    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("image/imageDB/"+str(count)+".jpg" ,imgRoi)
        cv2.rectangle(img , ( 0 ,200) , (640 ,300) , ( 0,255 , 0) ,cv2.FILLED)
        cv2.putText(img ,"Scan Saved" ,(150 , 265) ,cv2.FONT_HERSHEY_DUPLEX ,2 ,(0,0,255),2)
        cv2.imshow("Result" ,img)
        cv2.waitKey(5)
        count +=1
           # if cv2.waitKey(1) & 0xFF == ord('q'):
              #  break
