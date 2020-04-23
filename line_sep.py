# -*- coding: utf-8-sig -*-
import os
import re
import codecs

f = codecs.open( r"C:\Users\Igor\Desktop\issue_sorted.txt", "r", "utf-8" )

fd = f.readlines()

oldList = list(fd)

newList = []

for line in oldList:
    #если длина больше 20, но меньше 45 - делим на две строки
    #если больше 45 - делим на три строки
    #деление по строкам делаем с учетом полных слов(пробелов м/у словами)
    if len(line) > 20:
        k = 0
        if len(line) < 45:
            repeat = True

            for i in line:
                
                if  k >= round(len(line)/2) and i == ' ' and repeat == True:
                        line = line[:(k)] + '\n' + line[k+1:]
                        newList.append(line)
                        repeat = False
                
                k = k + 1

        else:
            k = 0
            repeat = True
            repeat1 = True
            for i in line:
                
                if  k >= round(len(line)/3) and i == ' ' and k < round(len(line)*(2/3)-1) and repeat == True:
                        line = line[:(k)] + '\n' + line[k+1:]
                        #newList.append(line)
                        repeat = False
                if  k >= round(len(line)*(2/3)) and i == ' ' and repeat1 == True:
                        line = line[:(k)] + '\n' + line[k+1:]
                        newList.append(line)
                        repeat1 = False

                k = k + 1

print(newList)

issue_sep = open(r"C:\Users\Igor\Desktop\issue_sep.txt",'w', encoding="utf-8")
for i in newList:
    i = i.replace("\r\n", "")
    issue_sep.write(i+'\n')
