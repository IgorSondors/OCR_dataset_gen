# -*- coding: utf-8-sig -*-
import numpy as np
import os
import sys
import cv2
from PIL import Image

image_source = r'C:\Users\Igor\Desktop\images'
crops_path = r'C:\Users\Igor\Desktop\crops'

file = r'C:\Users\Igor\Desktop\clean.txt'
os.chdir(crops_path)


def Writing_labelling_Crops(file):

    f=open(file,"r", encoding = 'utf8') 
    lines=f.readlines() 
    filename = [] 
    Xmin = []
    Ymin = []
    Xmax = []
    Ymax = []
    text = []
    for x in lines: 
        filename.append(x.split(';')[0]) 
        Xmin.append(int(x.split(';')[1]))
        Ymin.append(int(x.split(';')[2]))
        Xmax.append(int(x.split(';')[3]))
        Ymax.append(int(x.split(';')[4]))
        text.append((x.split(';')[5])[:-1])#Убрать из текстовых \n
    f.close()

    res = []
    heigh = []
    width = []
    H = []
    W = []
    
    for i in range(len(Xmin)):
        res.append([int(Xmin[i]), int(Ymin[i]), int(Xmax[i]), int(Ymax[i]), filename[i], text[i]])        
       
    print(len(res))

    for i in range(len(Xmin)):
        width.append(res[i][2] - res[i][0])
        heigh.append(res[i][3] - res[i][1])
        
        w = res[i][2] - res[i][0]
        W.append(w)
        h = res[i][3] - res[i][1]
        H.append(h)
        

        pts1 = np.float32([[res[i][0], res[i][1]], [res[i][2], res[i][1]], [res[i][2], res[i][3]], [res[i][0], res[i][3]]])
        pts2 = np.float32([[0,0],[W[i],0],[W[i],H[i]],[0,H[i]]])

        print(pts1, ',', pts2)

        M = cv2.getPerspectiveTransform(pts1,pts2)

        image_path = os.path.join(image_source, str(filename[i]))

        img = cv2.imread(image_path,3)

        dst = cv2.warpPerspective(img,M,(W[i], H[i]))



        crop_name = os.path.join(crops_path, text[i] + '_'+'{}'.format(i)+'.jpg')


        is_success, im_buf_arr = cv2.imencode(".jpg", dst)
        im_buf_arr.tofile(crop_name)



Writing_labelling_Crops(file)

