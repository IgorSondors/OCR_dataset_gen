# -*- coding: utf-8-sig -*-
#from Faker import Language ru_RU
import re 
from faker import Faker
fake = Faker(['ru_RU', 'ru_RU', 'ru_RU', 'ru_RU'])
#print(fake.address())

with open('ru.txt', 'w', encoding="utf8") as f:
    for i in range(1000):
            #место выдачи
            f.write('ТП №')
            f.write(str(fake.date(pattern='%d', end_datetime=None)))
            f.write(' ')
            x = (str(fake.address()))
            x = re.sub('[!@#$,/1234567890]', '', x) 
            x = x.replace("  ", "")
            f.write(x.upper())
            f.write('\n')
            #место выдачи
            f.write('УФМС ')
            f.write(str(fake.date(pattern='%d', end_datetime=None)))
            f.write(' ')
            y = (str(fake.address()))
            y = re.sub('[!@#$,/1234567890]', '', y) 
            y = y.replace("  ", "")
            f.write(y.upper())
            f.write('\n')
            #место выдачи
            z = (str(fake.address()))
            z = re.sub('[!@#$,/0456789]', '', z) 
            z = z.replace("  ", "")
            f.write(z.upper())
            f.write('\n')
            f.write(fake.first_name().upper())
            f.write('\n')
            f.write(fake.last_name().upper())
            f.write('\n')
            f.write(fake.middle_name().upper())
            f.write('\n')
            f.write(fake.city().upper())
            f.write('\n')
            f.write(fake.date(pattern='%d.%m.%Y', end_datetime=None))#дата рожд
            f.write('\n')
            f.write(fake.date(pattern='%Y-%Y', end_datetime=None))#код подразделения
            f.write('\n')
            f.write(fake.date(pattern='%d %m %m%m%m', end_datetime=None))#серия номер пасп
            f.write('\n')