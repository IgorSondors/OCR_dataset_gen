# coding=utf8
import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
#import tensorflow as tf
import zipfile
import cv2

from distutils.version import StrictVersion
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
import pytesseract
import Levenshtein as lv

mask = ['РОССИЙСКАЯ ФЕДЕРАЦИЯ','Паспорт выдан','Дата выдачи','Код подразделения','Личный код','Личная подпись','Фамилия','Имя','Отчество','Пол']
two_strings_mask = ['Дата рождения','Место рождения']

text = ['россии скАЯ орла цИиЯя', 'ЧП #62 МЕЖРАЙОННОГО ОТДЕЛА №2 УФИС РОССИЯ ПО', 'Паспорт ван', 'САНКТ-ЛЕТЕРВУРГУ И ЛЕНИНГРАДСКОЙ ов1. (ОБСЛУЖИВАЕТ ПЕТРОДВОРНОВЫЙ |', 'р-й Г. САНКТ-ПЕТЕРВУРГА И ЛОМОНОСОВСКИЙ Р-Н ЛЕНИНГРАДСКОЙ ов.)', '780—095', '7.0.2015', 'Кол подразделения.', 'Лата вылачи.', 'Личный Код.', 'Аинная фев', 'СОНДОРС', '| Фамилия', 'ИГОРЬ', 'Имя.', 'Отчество.', 'КОНСТАНТИНОВИЧ', 'МУЖ.', 'Пол', '14.09.1994', 'к', 'ГОР. ЕКАТЕРИНБУРГ', 'Е']


#Замена слов маски паспорта по наименьшему расстоянию Левенштейна

txt_store = []

for n in range(len(text)):
    txt_store.append(text[n])
print(txt_store)

for j in range(len(mask)):
    dist = []
    
    for i in range(len(text)):
        dist.append(lv.distance(text[i], mask[j]))
        
    min_dist = min(dist)
    min_dist_ind = dist.index(min_dist)
    
    text.pop(min_dist_ind)
    text = text.insert(min_dist_ind, '###################################')
    #print(min_dist_ind, text[min_dist_ind])
    print(text)
    del  txt_store[min_dist_ind]
    txt_store.insert(min_dist_ind, mask[j])
        
        
    print('min_dist:' , min_dist)
    #print('min_dist_ind:', min_dist_ind, text[min_dist_ind], '-->', txt_store[min_dist_ind]) 
        
    print('dist между mask номер', j, 'и text:', dist, len(dist))  

print()
print(text, len(text))
print()
#print(text, len(text))
print()
print(txt_store, len(txt_store))

