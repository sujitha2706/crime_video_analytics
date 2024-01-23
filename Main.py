#from call_the_police import Model
from mail import send_mail
from label_image import predict #predict lables of data values on basis of trained model-->accepts single arg
import numpy as np
import cv2    # computer vision prob
import os  

def Test_Video(filename):
    detection_count = 0
    cap = cv2.VideoCapture(filename)   #read vedio

    while True:
        ret,frame = cap.read() #read->returns bool,frame read correctly
         #INFINITE LOOP-->BREAK by break stmt-->ret-boolean (frame availability),frame-get next frame(array vector)
        cv2.imwrite('proof'+str(detection_count+1)+'.png',frame)  #save img to storage-->particular format
        crime = predict('proof1.png')
        #print(crime)
        if crime != 0:
            detection_count += 1
            print(detection_count)

            if detection_count >= 2:
            #   send_mail(crime,'proof1.png','proof2.png')
                detection_count = 0
        else:
            os.remove('proof1.png')  #remove or delete file path

def Live_Cam():

    cap = cv2.VideoCapture(0) #webcam access 0 rtsp url

    while True:
        ret,frame = cap.read()
def main():
    Test_Video('4.mp4')
        #Live_Cam()
if __name__ == '__main__':
    main()



