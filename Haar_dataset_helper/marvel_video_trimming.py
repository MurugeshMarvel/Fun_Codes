#!/usr/bin/python
import cv2
import sys
import glob
import time
import os

debug = 1
obj_list = []
obj_count = 0
click_count = 0
x1 = 0
y1 = 0
h = 0
w = 0
key = None
frame = None


def crop(frame,name):
    x2 = x1 + w
    y2 = y1 + h
    image = frame[y1:y2 , x1:x2]
    cv2.imwrite(name, image)
def obj_marker(event,x,y,flags,param):
    global click_count
    global debug
    global obj_list
    global obj_count
    global x1
    global y1
    global w
    global h
    global frame
    if event == cv2.EVENT_LBUTTONDOWN:
        click_count += 1
        if click_count % 2 == 1:
            x1 = x
            y1 = y
        else:
            w = abs(x1 - x)
            h = abs(y1 - y)
            obj_count += 1
            if x1 > x:
                x1 = x
            if y1 > y:
                y1 = y
            obj_list.append('%d %d %d %d ' % (x1,y1,w,h))
            cv2.rectangle(frame,(x1,y1),(x1+w,y1+h),(255,0,0),1)
            cv2.imshow('frame',frame)


#creating window for frame and setting mouse callback
if __name__ == '__main__':
    file_name = raw_input("Enter the file to be opened")
    video_file = str(file_name) + '.avi'
    index2 = 0
    folder_name = file_name + '_cropped'
    if folder_name in os.listdir(os.curdir):
        pass
    else:
        os.system("mkdir %s"%folder_name)
    cv2.namedWindow('frame',cv2.WINDOW_AUTOSIZE)
    annotate_file = open('annotate.txt','a')
    cv2.setMouseCallback('frame',obj_marker)
    cap = cv2.VideoCapture(video_file)
    #creating a file handle
    index = 0
    frame_id = 0
    
    #loop to traverse through all the files in given path
    while True:
        
        ret, frame = cap.read()
        main_frame = frame
        cv2.imshow('frame',frame)
        obj_count = 0
        key = cv2.waitKey(0)
        print "Key is " ,key
        if key == 65364:
        	print "hi"
    		fi = "negatives_" + file_name
    		os.system("mkdir %s" %fi)
    		nega_file = fi+ "/" + "image"+ str(index) +".jpg"
    		cv2.imwrite(nega_file,frame)
        
        while((key & 0xFF != ord('q')) and key != 65364 and key != 65363):
            index_c = str(index) + "-" + str(index2)
            key = cv2.waitKey(0)
            if(key & 0xFF == ord('c')):
                obj_count = 0
                obj_list = []
                print x1,y1,w,h
                file = file_name + '-'+str(index_c)
                save_file = folder_name + '/' + file + '.jpg'
                crop(main_frame, save_file)
                content = file + "\t" + str(x1) + '\t' + str(y1) + '\t' + str(w) + '\t' +str(h)
                annotate_file.write(content)
                annotate_file.write('\n')
                cv2.imshow('frame',frame)
                index2 += 1
                print index_c

    	

        if(key & 0xFF == ord('q')):
            break

        elif(key == 65363):
            index2=0
            index_c = str(index) + "-" + str(index2)
            if(obj_count > 0):
                for j in obj_list:
                    file = file_name + '-'+str(index_c)
                    save_file = folder_name + '/' + file + '.jpg'
                    content = file + "\t" + str(x1) + '\t' + str(y1) + '\t' + str(w) + '\t' +str(h)
                    annotate_file.write(content)
                    annotate_file.write('\n')
                    crop(frame, save_file)
                    print index_c
                obj_count = 0
                obj_list = []
        

        index += 1
    annotate_file.close()
    cv2.destroyAllWindows()
