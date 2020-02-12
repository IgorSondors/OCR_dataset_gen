################### Создаем annotation.txt
import os
import re


annotations = []

for d, dirs, files in os.walk('/home/sonders/shared/synth/out'):

    for f in files:
        path = os.path.join(d,f) # формирование адреса
        annotations.append(path) # добавление адреса в список

# Формирование списка Id каждого изображения (regular expressions)
#Id = re.findall(r'_(\w+)', str(annotations)) #Считывание цифр перед .jpg
Id = re.findall(r'_(\d+).jpg', str(annotations))


#print(Id)
#print(len(Id))

# Запись списка полных путей к изображениям + разделения столбца (;) в txt по строкам
ann = open("annotation.txt",'w', encoding="utf8")
for i in range(len(annotations)):
    ann.write(annotations[i]+';'+ Id[i] +'\n')