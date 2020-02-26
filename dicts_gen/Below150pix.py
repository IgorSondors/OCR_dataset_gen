# -*- coding: utf-8-sig -*-
#from Faker import Language ru_RU
import re 
from faker import Faker
fake = Faker(['ru_RU', 'ru_RU', 'ru_RU', 'ru_RU'])
#print(fake.address())

with open('150ru.txt', 'w', encoding="utf8") as f:
    for i in range(15000):#*13
        f.write(fake.date(pattern='%d.%m.%Y', end_datetime=None))#дата рожд
        f.write('\n')
        f.write(fake.date(pattern='%Y-%Y', end_datetime=None))#код подразделения
        f.write('\n')
        first_name = fake.first_name().upper()
        if len(first_name) < 9:
            f.write(first_name)
            f.write('\n')
        last_name = fake.last_name().upper()    
        if len(last_name) < 9:
            f.write(last_name)
            f.write('\n')
        f.write('МУЖ.')
        f.write('\n')
        f.write('ЖЕН.')
        f.write('\n')
        city = fake.city().upper()
        if len(city) < 9:
            f.write(city)
            f.write('\n')
        f.write(fake.date(pattern='%d.%m.%Y', end_datetime=None))#дата рожд
        f.write('\n')
        f.write(fake.date(pattern='%Y-%Y', end_datetime=None))#код подразделения
        f.write('\n')
        f.write('Фамилия')
        f.write('\n')
        f.write('Имя')
        f.write('\n')
        f.write('Отчество')
        f.write('\n')
        f.write('Пол')
        f.write('\n')

################# Обратить внимание на количество сгенерированных строк. Сделать кратно 100