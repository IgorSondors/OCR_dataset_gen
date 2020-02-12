# -*- coding: utf-8-sig -*-
# Запись lexicon с порядком слов в тхт в соответствии с их Id(на единицу больше, так как строки начинаются с 1, а Id с 0) как в оригинальном датасете
import os
import re
path_f = []

for d, dirs, files in os.walk('/home/sonders/shared/synth/out'):
    path_f.append(files)

#print(path_f)
path_f = path_f[0]

Dic = {}
for i in path_f:
    dic1 = {int(re.findall(r'_(\w+)_', i)[0]):i[:-(len(re.findall(r'_(\w+)_', i)[0])+5)]}
    Dic.update(dic1)
    
#print(Dic)

lexicon_true = []
for k in range(len(path_f)):
    lexicon_true.append(Dic.get(k)) 

# Запись списка полных путей к изображениям в txt по строкам
l = open("lex.txt",'w', encoding="utf8")
for i in lexicon_true:
    l.write(i+'\n')


