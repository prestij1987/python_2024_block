vozr= input('Ваш возраст; ')
age = int(vozr)
res = 0

while age > 0:
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
            print('Ошибка данных') 

