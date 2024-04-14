# 1. На строке 43 заменить конкатенацию на форматирование
# concat, concatenate, конкатенация - "сложение плюсиком"
# 2. Написать тест по математике.
#    генерить примеры на +, -, *
#    проверки хранить в виде функций
#    к функции проверки обращаться по ключу-действию, собрав их в словарь!
#    внешний цикл предлагает решить ещё один пример, либо завершить тест.
#    выводится статистика.
#  
def greet(name, fathername):
    return 'Здравствуйте' # сделать подстановку через функцию

print(greet('Игорь', 'Иванович'))  # передача параметров по ПОЗИЦИИ
print(greet('Иванович', 'Игорь'))  # передача параметров по ПОЗИЦИИ

def osnova(): # основной внешний цикл
    chislo_one = input('Введите число один: ')
    chislo_two = input('Введите число два: ')

    chislo_1 = int(chislo_one)
    chislo_2 = int(chislo_two)

    dict_primer = {'sloj': '+', 
                'vychit': '-','ymnoj': '*'}
    add = 'finish'

    while  add != 'finish':
        while  10 > chislo_1 > 0 and 10 > chislo_2 > 0:

            def work_dict(comand):   # Создание функции работы со словарем
                dict_primer([comand])

                work_dict(comand.key)

            def sloj (znak1, znak2):
                return znak1 + znak2
            
            sloj(chislo_1, chislo_2)
            print(sloj(chislo_1, chislo_2))


            def vychit (znak1, znak2):
                return znak1 - znak2
            
            sloj(chislo_1, chislo_2)
            print(sloj(chislo_1, chislo_2))
            try: 
                chislo_1 == chislo_2    
            except NameError:
                print('Вы ввели две одиковые цифры попробуйте еще раз')
                
osnova()
