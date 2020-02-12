import codecs
import os
import re
################### Создаем imlist.txt

path_f = []

for d, dirs, files in os.walk('/home/sonders/shared/synth/out'):

    for f in files:
        path = os.path.join(d,f) # формирование адреса
        path_f.append(path) # добавление адреса в список


# Запись списка полных путей к изображениям в txt по строкам
l = open("imlist.txt",'w', encoding="utf8")
for i in path_f:
    l.write(i+'\n')





################### Создаем annotation.txt

annotations = []

for d, dirs, files in os.walk('/home/sonders/shared/synth/out'):

    for f in files:
        path = os.path.join(d,f) # формирование адреса
        annotations.append(path) # добавление адреса в список

# Формирование списка Id каждого изображения (regular expressions)
#Id = re.findall(r'_(\w+)', str(annotations)) #Считывание цифр перед .jpg
Id = re.findall(r'_(\w+).jpg', str(annotations))


#print(Id)
#print(len(Id))

# Запись списка полных путей к изображениям + разделения столбца (;) в txt по строкам
ann = open("annotation.txt",'w', encoding="utf8")
for i in range(len(annotations)):
    ann.write(annotations[i]+';'+ Id[i] +'\n')
