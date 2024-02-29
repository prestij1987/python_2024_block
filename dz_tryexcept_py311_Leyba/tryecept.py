'''vozr= input('Ваш возраст; ')
age = int(vozr)
res = 0
year =2024

while age > 20 and age < 100:
    res = age + 1
    if res == 10:
        print('Цикл закончен')
    try:
        if age < 0 and age < 100:
            print('Введите ваш возраст')
    except ZeroDivisionError:
       ## if age < 0 and age < 100:
            print('Возраст отрицательный ')
    except NameError:
            print('Ошибка данных')'''

'''birth_year = int(input('Какой твой год рождения?'))
if birth_year < 1800:
    raise ValueError(
        'Ты - исторический персонаж? Столько не живут')'''

# Исправьте программу, запрашивающую год рождения с добавлением собственного исключения

born = input('Введите ваш год рождения: ')
born_1 =  2024 - int(born)
try:
    if born_1 < 80 and born_1 < int(-1):
        raise ValueError('Ты не родился ')
    print('Попробуй еще: ')
except ZeroDivisionError:
    print('Ошибка произошла ')