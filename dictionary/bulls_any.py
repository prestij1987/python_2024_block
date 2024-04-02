from random import randint
from random import choice

# Быки и коровы - дописать игру!

# бык - цифра, которая стоит на своем месте
# корова - цифра, которая есть, но на чужом месте

fin = 'finish'
while fin != 'finish':
    bulls = 0
    cows = 0
    chislo = choice.randint(list(1,9))
    
    chislo_out = int(input('Введите трех значное число: '))
    for perebor in chislo:
        if perebor[perebor] == chislo[perebor]:
            bulls += 1
        elif perebor in chislo:
            cows += 1    
        elif perebor != 'int':
            print('Вы ввели не число попробуйте еще раз: ')
    print(cows, bulls)            
    