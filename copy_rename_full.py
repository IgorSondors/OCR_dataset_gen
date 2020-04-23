import os
import glob
from shutil import copyfile

os.chdir(r'C:\Users\Igor\Desktop\Dataset_mask\Дата рождения')
for index, oldfile in enumerate(glob.glob("*.jpg"), start=28000):
    newfile = ('Дата рождения'+'_'+'{}'+'.jpg').format(index)
    copyfile(oldfile, os.path.join(r'C:\Users\Igor\Desktop\out', newfile))

os.chdir(r'C:\Users\Igor\Desktop\Dataset_mask\Дата выдачи')
for index, oldfile in enumerate(glob.glob("*.jpg"), start=29000):
    newfile = ('Дата выдачи'+'_'+'{}'+'.jpg').format(index)
    copyfile(oldfile, os.path.join(r'C:\Users\Igor\Desktop\out', newfile))

os.chdir(r'C:\Users\Igor\Desktop\Dataset_mask\ЖЕН')
for index, oldfile in enumerate(glob.glob("*.jpg"), start=30000):
    newfile = ('ЖЕН.'+'_'+'{}'+'.jpg').format(index)
    copyfile(oldfile, os.path.join(r'C:\Users\Igor\Desktop\out', newfile))

os.chdir(r'C:\Users\Igor\Desktop\Dataset_mask\Имя')
for index, oldfile in enumerate(glob.glob("*.jpg"), start=31000):
    newfile = ('Имя'+'_'+'{}'+'.jpg').format(index)
    copyfile(oldfile, os.path.join(r'C:\Users\Igor\Desktop\out', newfile))

os.chdir(r'C:\Users\Igor\Desktop\Dataset_mask\Код подразделения')
for index, oldfile in enumerate(glob.glob("*.jpg"), start=32000):
    newfile = ('Код подразделения'+'_'+'{}'+'.jpg').format(index)
    copyfile(oldfile, os.path.join(r'C:\Users\Igor\Desktop\out', newfile))

os.chdir(r'C:\Users\Igor\Desktop\Dataset_mask\Личная подпись')
for index, oldfile in enumerate(glob.glob("*.jpg"), start=33000):
    newfile = ('Личная подпись'+'_'+'{}'+'.jpg').format(index)
    copyfile(oldfile, os.path.join(r'C:\Users\Igor\Desktop\out', newfile))

os.chdir(r'C:\Users\Igor\Desktop\Dataset_mask\Личный код')
for index, oldfile in enumerate(glob.glob("*.jpg"), start=34000):
    newfile = ('Личный код'+'_'+'{}'+'.jpg').format(index)
    copyfile(oldfile, os.path.join(r'C:\Users\Igor\Desktop\out', newfile))

os.chdir(r'C:\Users\Igor\Desktop\Dataset_mask\Место рождения')
for index, oldfile in enumerate(glob.glob("*.jpg"), start=35000):
    newfile = ('Место рождения'+'_'+'{}'+'.jpg').format(index)
    copyfile(oldfile, os.path.join(r'C:\Users\Igor\Desktop\out', newfile))

os.chdir(r'C:\Users\Igor\Desktop\Dataset_mask\МУЖ')
for index, oldfile in enumerate(glob.glob("*.jpg"), start=36000):
    newfile = ('МУЖ.'+'_'+'{}'+'.jpg').format(index)
    copyfile(oldfile, os.path.join(r'C:\Users\Igor\Desktop\out', newfile))

os.chdir(r'C:\Users\Igor\Desktop\Dataset_mask\Отчество')
for index, oldfile in enumerate(glob.glob("*.jpg"), start=37000):
    newfile = ('Отчество'+'_'+'{}'+'.jpg').format(index)
    copyfile(oldfile, os.path.join(r'C:\Users\Igor\Desktop\out', newfile))

os.chdir(r'C:\Users\Igor\Desktop\Dataset_mask\Паспорт выдан')
for index, oldfile in enumerate(glob.glob("*.jpg"), start=38000):
    newfile = ('Паспорт выдан'+'_'+'{}'+'.jpg').format(index)
    copyfile(oldfile, os.path.join(r'C:\Users\Igor\Desktop\out', newfile))

os.chdir(r'C:\Users\Igor\Desktop\Dataset_mask\Пол')
for index, oldfile in enumerate(glob.glob("*.jpg"), start=39000):
    newfile = ('Пол'+'_'+'{}'+'.jpg').format(index)
    copyfile(oldfile, os.path.join(r'C:\Users\Igor\Desktop\out', newfile))

os.chdir(r'C:\Users\Igor\Desktop\Dataset_mask\Фамилия')
for index, oldfile in enumerate(glob.glob("*.jpg"), start=40000):
    newfile = ('Фамилия'+'_'+'{}'+'.jpg').format(index)
    copyfile(oldfile, os.path.join(r'C:\Users\Igor\Desktop\out', newfile))


