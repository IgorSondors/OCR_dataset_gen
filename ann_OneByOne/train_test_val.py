################### Делим annotation.txt на train, test, val .txt
import codecs
import os
import re

f = codecs.open( "annotation.txt", "r", "utf-8-sig" )
fd = f.readlines()

new_fd = list(fd)

'''#print(new_fd)

mask_fd = []
for i in new_fd:
    print(i)
    if (re.findall('Имя', str(i))).group(0) == 'Имя':
        #i = i.replace("\r\n", "")
        mask_fd.append(i)
        new_fd.remove(i)
        print(mask_fd)
    
print()
    

train_fd = []
train_fd = train_fd + mask_fd

test_fd = []

val_fd = []

train = open("annotation_train.txt",'w')

for i in train_fd:
    train.write(i)

#test = open("annotation_test.txt",'w')
#val = open("annotation_val.txt",'w')
print('111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')

'''

########################### Тупо делим сырой список на три части без предварительной обработки (проверка работоспособности обучения сетки)#####################################

x = len(new_fd)

train_fd = new_fd[:round(x*0.8)]
test_fd = new_fd[round(x*0.8):round(x*0.95)]
val_fd = new_fd[round(x*0.95):]



train = open("annotation_train.txt",'w', encoding="utf8")
for i in train_fd:
    i = i.replace("\r\n", "")
    train.write(i)


test = open("annotation_test.txt",'w', encoding="utf8")

for i in test_fd:
    i = i.replace("\r\n", "")
    test.write(i)

val = open("annotation_val.txt",'w', encoding="utf8")

for i in val_fd:
    i = i.replace("\r\n", "")
    val.write(i)