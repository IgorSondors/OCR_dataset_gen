#from Faker import Language ru_RU
import re 
from faker import Faker
fake = Faker(['ru_RU', 'ru_RU', 'ru_RU', 'ru_RU'])
#print(fake.address())

with open('ru.txt', 'w') as f:
    for i in range(500):
        #место выдачи
        f.write('УФМС ')
        f.write(str(fake.date(pattern='%d', end_datetime=None)))
        f.write('\n')
        f.write(fake.first_name().upper())
        f.write('\n')
        f.write(fake.last_name().upper())
        f.write('\n')
        f.write(fake.middle_name().upper())
        f.write('\n')
        f.write('МУЖ.')
        f.write('\n')
        f.write('ЖЕН.')
        f.write('\n')
        f.write(fake.city().upper())
        f.write('\n')
        f.write(fake.date(pattern='%d.%m.%Y', end_datetime=None))#дата рожд
        f.write('\n')
        f.write(fake.date(pattern='%Y-%Y', end_datetime=None))#код подразделения
        f.write('\n')
        f.write(fake.date(pattern='%d %m %m%m%m', end_datetime=None))#серия номер пасп
        f.write('\n')
        f.write('Паспорт выдан')
        f.write('\n')
        f.write('Дата выдачи')
        f.write('\n')
        f.write('Код подразделения')
        f.write('\n')
        f.write('Личный код')
        f.write('\n')
        f.write('Личная подпись')
        f.write('\n')
        f.write('Фамилия')
        f.write('\n')
        f.write('Имя')
        f.write('\n')
        f.write('Отчество')
        f.write('\n')
        f.write('Пол')
        f.write('\n')

    for i in range(2000):
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