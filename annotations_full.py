# -*- coding: utf-8-sig -*-
import glob
import os
import re
import codecs

synth_out = '/home/sonders/shared/synth/out'

#1) Запись lexicon с порядком слов в тхт в соответствии с их Id(на единицу больше, так как строки начинаются с 1, а Id с 0) как в оригинальном датасете

path_lexicon = []

for d, dirs, files in os.walk(synth_out):
    path_lexicon.append(files)

#print(path_lexicon)
path_lexicon = path_lexicon[0]

Dic = {}
for i in path_lexicon:
    dic1 = {int(re.findall(r'_(\w+)', i)[0]):i[:-(len(re.findall(r'_(\w+)', i)[0])+5)]}
    Dic.update(dic1)
    
#print(Dic)

lexicon_true = []
for k in range(len(path_lexicon)):
    lexicon_true.append(Dic.get(k)) 

# Запись списка полных путей к изображениям в txt по строкам
l = open("/home/sonders/OpenCV/tesseract/lexicon.txt",'w', encoding="utf8")
for i in lexicon_true:
    l.write(i+'\n')


##2) Renaming

os.chdir(synth_out)
for index, oldfile in enumerate(glob.glob("*.jpg"), start=1):
    newfile = ('{}'+'_'+oldfile).format(index)
    os.rename (oldfile,newfile)


##3) Создаем imlist.txt
################### Создаем imlist.txt

path_imlist = []

for d, dirs, files in os.walk(synth_out):

    for f in files:
        path = os.path.join(d,f) # формирование адреса
        path_imlist.append(path) # добавление адреса в список


#print('imlist:', path_imlist)
# Запись списка полных путей к изображениям в txt по строкам
l = open("/home/sonders/OpenCV/tesseract/imlist.txt",'w', encoding="utf8")
for i in path_imlist:
    l.write(i+'\n')


##4) Создаем annotation.txt

################### Создаем annotation.txt

list_annotation = []

for d, dirs, files in os.walk(synth_out):

    for f in files:
        path = os.path.join(d,f) # формирование адреса
        list_annotation.append(path) # добавление адреса в список

# Формирование списка Id каждого изображения (regular expressions)
#Id = re.findall(r'_(\w+)', str(list_annotation)) #Считывание цифр перед .jpg
Id = re.findall(r'_(\d+).jpg', str(list_annotation))

#print('list_annotation: ', list_annotation)
#print(len(list_annotation))
#print('Id for list_annotation: ', Id)
#print(len(Id))

# Запись списка полных путей к изображениям + разделения столбца (;) в txt по строкам
ann = open("/home/sonders/OpenCV/tesseract/annotation.txt",'w', encoding="utf8")
for i in range(len(list_annotation)):
    ann.write(list_annotation[i]+';'+ Id[i] +'\n')

##5) Делим annotation.txt на train, test, val .txt


# Другой скрипт