# -*- coding: utf-8-sig -*-
import glob
import os
import re
import codecs

################### Делим annotation.txt на train, test, val .txt

f = codecs.open( "/home/sonders/OpenCV/tesseract/annotation.txt", "r", "utf-8-sig" )

fd = f.readlines()

new_fd = list(fd)


########################### Тупо делим сырой список на три части без предварительной обработки (проверка работоспособности обучения сетки)#####################################

x = len(new_fd)

train_fd = new_fd[:round(x*0.8)]
test_fd = new_fd[round(x*0.8):round(x*0.95)]
val_fd = new_fd[round(x*0.95):]

#print(new_fd)
#print(train_fd)
#print(test_fd)
#print(val_fd)

train = open("/home/sonders/OpenCV/tesseract/annotation_train.txt",'w', encoding="utf8")
for i in train_fd:
    i = i.replace("\r\n", "")
    train.write(i)


test = open("/home/sonders/OpenCV/tesseract/annotation_test.txt",'w', encoding="utf8")

for i in test_fd:
    i = i.replace("\r\n", "")
    test.write(i)

val = open("/home/sonders/OpenCV/tesseract/annotation_val.txt",'w', encoding="utf8")

for i in val_fd:
    i = i.replace("\r\n", "")
    val.write(i)