
'''1. Найти и показать работу функции, определяющей размер файла.
8 баллов
2. Найти и показать работу функции, определяющей время файла
10 баллов
3**. 12 12
Посчитать объем директории без использования shutil
циклом и рекурсией. Обязательно использовать try..'''

import os
from datetime import time

with open('dz_files.txt', 'r', encoding='utf-8') as my_file:
   file_size = os.path.getsize('dz_files.txt')
   print('Размер файла:', file_size, 'байт')

#  Не работает как запустить не знаю
def time_func():
   with open('dz_files.txt', 'r', encoding='utf-8') as my_file:
      time_work = my_file.time.time()
   print(time_work.now)