# -*- coding: utf-8-sig -*-
import codecs

# Читаем предварительно сохраненный в кодировке ютф8 словарь
f = codecs.open( "ru.txt", "r", "utf-8-sig" )
fd = f.readlines()
l = open("lexicon.txt",'w', encoding="utf8")

# Удаление повторяющихся строк в неотсортированном списке
new_fd = list(set(fd))


# Очищенный от повторов новый список сортируем по длине строк
new_fd = sorted(new_fd, key=lambda a: len(a))

# Удаление лишних отступов абзаца
for i in new_fd:
    i = i.replace("\r\n", "")
    l.write(i+'\n')





'''l = open("lexicon.txt",'w')
l.writelines(i for i in new_fd)
l.close()'''
