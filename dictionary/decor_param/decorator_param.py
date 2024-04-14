#Написать функцию-декоратор, выводящую на печать количество возвращённых значений
#Написать функцию-декоратор, выводящую на печать количество принятых параметров
#Написать функцию-декоратор, делающую вызов любой функции "безопасным", но сообщающую на экран о произошедшей ошибке
#Применить к одной функции два декоратора: измерения времени и "обезопашивания". Какой нужно применять первым?ы


def decor_func():
    def func1(): # Создание фунции
        def param(*args, **kwargs): # создаенем функции с аргументом и параметром
            result =  func1(*args, *kwargs)
            print(f'Функция вернула, {len(result)} значений')
            return result
        return param
    return func1
def count(func1):  # функция которая вводит количество принятых параметров
    chet = 0
    if chet > 0 and chet < 10:
        chet += 1
    result_2 = chet    
    print(f'Количество вхождений функции %s {result_2}')
    

@decor_func
def decor(count):

        print('Произошла ошибка ')
decor()    

#первая функция
'''def decorator_function(func):
    def python():
        print("Первая функция")
        print("обрабатываемая функция {}".format(func))
        print("выполняем функцию")
        func()
        print("Выходим из функции")
    return python

@decorator_function
def first_decorator():
    print("first_decorator")

first_decorator()'''