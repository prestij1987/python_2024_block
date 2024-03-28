import random
#Создать игру поле чудес
import dict_word

# slovo = ['колесо', 'замок', 'золото', 'тарелка']

#zapros = input('Загадай одно из слов', slovo)
#zapros1 = random.choice(list(dict_word)) cлучайное слово из словаря
zapros1 = list(dict_word)
otvet = ''

while zapros1 != otvet:
    otvet =+ input( f'введите букву: ')
    if zapros1 == otvet:
        hide_word = '_' * len(zapros1) 
        print('Вы отгадали слово', hide_word)    
     




