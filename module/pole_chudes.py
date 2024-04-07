import random
#Создать игру поле чудес
from dict_world import zagadka

zapros1 = list(zagadka)
otvet = ''

while zapros1 != otvet:
    otvet =+ input( f'введите букву: ')
    for i in zapros1:
        for it in otvet:

            if zapros1[i] == otvet[it]:
                print('Печатаем букву ')
            else:
                print('Ввели неправильное букву ппробуйте еще раз ')    
          
                hide_word = '_' * len(zapros1) 
    print('Вы отгадали слово', hide_word)    
     




