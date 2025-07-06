import cv2    
from mysql_connection import connect                                                      
face_cap = cv2.CascadeClassifier("C:/Users/sumit/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml")       # model for human face impresion and cascadeclassifier tool for reading image like eyes nose  
video_cap = cv2.VideoCapture(0)        #open default camera enable infinite time:

#take input only once before loop:
name=input('enter a employee name:')
address=input('enter a employee address:')
status="present"
inserted= False      #flag insert only once
if not video_cap.isOpened():          
    print("Error: Cannot open webcam")
else:
    while True:
        ret, video_data = video_cap.read()   #  ret true or false(frame found ya not)& store it video_data
        color= cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)      # video data black and white
        
        faces= face_cap.detectMultiScale(                     # faces factor
            color,
            scaleFactor=1.1,                     #scanning
            minNeighbors=5,
            minSize=(30,30),                     #object face crieteria
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for(x,y,h,w) in faces:                             #rectangle perammetars
            cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2 )
            if not inserted:
                  conn=connect()
                  cur=conn.cursor()
                  cur.execute('INSERT INTO EMPLOYEES(name,address,status) VALUES(%s,%s,%s)',(name,address,status))
                  conn.commit()
                  conn.close()
                  print(f"Employee {name} marked as Present and added to database.")
                  inserted = True  # only once

        cv2.imshow("video_live", video_data)

        if cv2.waitKey(10) == ord("c"):  # Press 'c' to close
            break

video_cap.release()
cv2.destroyAllWindows()            # relese captured image
            

           