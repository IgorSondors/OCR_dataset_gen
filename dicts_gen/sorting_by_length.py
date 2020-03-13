# -*- coding: utf-8-sig -*-
import glob
import os
import re
import codecs

f = codecs.open( r"C:\Users\sondors\Desktop\dataset\unit.txt", "r", "utf-8-sig" )

fd = f.readlines()

new_fd = list(fd)

sortList = new_fd
def sortByLength(inputStr):
  return len(inputStr)

newList = sorted(sortList, key=sortByLength)

########################### Тупо делим сырой список на три части без предварительной обработки (проверка работоспособности обучения сетки)#####################################
train = open(r"C:\Users\sondors\Desktop\dataset\unit_sorted.txt",'w', encoding="utf8")
for i in newList:
    i = i.replace("\r\n", "")
    train.write(i+'\n')

