# -*- coding: utf-8-sig -*-
#from Faker import Language ru_RU
import re 
from faker import Faker
fake = Faker(['ru_RU', 'ru_RU', 'ru_RU', 'ru_RU'])

with open('ru400.txt', 'w', encoding="utf8") as f:
    for i in range(3000):
        f.write('Р О С С И Й С К А Я  Ф Е Д Е Р А Ц И Я')
        f.write('\n')
    for i in range(1000):
        f.write('\n')
        f.write('(ОБСЛУЖИВАЕТ Г.САНКТ-ПЕТЕРБУРГ И ЛОМОНОСОВСКИЙ Р-Н ЛЕНИНГРАДСКОЙ ОБЛ.)')
    for i in range(6000):
        #место выдачи
        f.write('ТП №')
        f.write(str(fake.date(pattern='%d', end_datetime=None)))
        f.write(' ')
        x = (str(fake.address()))
        x = re.sub('[!@#$,/1234567890]', '', x)
        x = x.replace("  ", "") 
        f.write(x.upper())
        f.write('\n')#1
        #место выдачи
        f.write('УФМС ')
        f.write(str(fake.date(pattern='%d', end_datetime=None)))
        f.write(' ')
        y = (str(fake.address()))
        y = re.sub('[!@#$,/1234567890]', '', y) 
        y = y.replace("  ", "")
        f.write(y.upper())
        f.write('\n')#2
        #место выдачи
        z = (str(fake.address()))
        z = re.sub('[!@#$,/0456789]', '', z)
        z = z.replace("  ", "") 
        f.write(z.upper())
        f.write('\n')#3
    for i in range(22500):
        #место выдачи
        f.write('ТП №')
        f.write(str(fake.date(pattern='%d', end_datetime=None)))
        f.write(' ')
        x = (str(fake.address()))
        x = re.sub('[!@#$,/1234567890]', '', x) 
        x = x.replace("  ", "")
        f.write(x.upper())
        f.write('\n')#1
        #место выдачи
        f.write('УФМС ')
        f.write(str(fake.date(pattern='%d', end_datetime=None)))
        f.write(' ')
        y = (str(fake.address()))
        y = re.sub('[!@#$,/1234567890]', '', y) 
        y = y.replace("  ", "")
        f.write(y.upper())
        f.write('\n')#2
        #место выдачи
        z = (str(fake.address()))
        z = re.sub('[!@#$,/0456789]', '', z) 
        z = z.replace("  ", "")
        f.write(z.upper())
        f.write('\n')#3
        #
        f.write('ОТДЕЛОМ УФМС ПО ')
        f.write(fake.city().upper())
        f.write('\n')#4
        f.write('ОТДЕЛОМ МИЛИЦИИ ПО ')
        f.write(fake.city().upper())
        f.write('\n')#5