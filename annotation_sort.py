from operator import itemgetter, attrgetter, methodcaller
import re
import codecs
#import zip



#x = []
f = codecs.open( "/home/sondors/CRNN_Tensorflow_Ubuntu18/data/annotations_Over400pix/annotation.txt", "r", "utf-8-sig" )

fd = f.readlines()

#new_fd = list(fd)

x = list(fd)

#sort_list = sorted(x, key=itemgetter(int(re.findall(r';(\w+)')), reverse=False))
ord_list = []
for i in x:
    ord_list.append(int(re.findall(r';(\w+)', i)[0]))
    
#print(ord_list)

#соединим два списка специальной функцией zip
X = zip(ord_list,x)

#x теперь [(3, 'a'), (1, 'b'), (2, 'c')]

#отсортируем, взяв первый элемент каждого списка как ключ
xs = sorted(X, key=lambda tup: tup[0])

#xs = [(1, 'b'), (2, 'c'), (3, 'a')]

#и последний шаг - извлечем
a1 = [X[0] for X in xs]
b1 = [X[1] for X in xs]

print(b1)

ann = open("/home/sondors/CRNN_Tensorflow_Ubuntu18/data/annotations_Over400pix/annotation_sorted.txt",'w', encoding="utf8")
for i in range(len(b1)):
    ann.write(b1[i])