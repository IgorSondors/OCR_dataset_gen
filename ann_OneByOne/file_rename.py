import os
import glob

os.chdir('/home/sonders/Рабочий стол/shared/synth/out')
for index, oldfile in enumerate(glob.glob("*.jpg"), start=1):
    newfile = ('{}'+'_'+oldfile).format(index)
    os.rename (oldfile,newfile)