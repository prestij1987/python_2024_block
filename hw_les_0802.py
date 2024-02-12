
'''Домашнее задание:
установить и настроить питон.

Задача 1.
Вводится количество и стоимость товара.
Посчитать сумму за товар.

Задача 2.
Вводится количество минут до урока
и расстояние в километрах.
Какая должна быть средняя скорость,
чтобы успеть на урок?

Задача 3. Вводится ширина, длина и высота комнаты.
Рулон обоев 10 метров при ширине 0.5
Сколько рулонов надо купить?'''

#Zadacha 1

kolvo_item = int(input('Vvedite kolvo tovara: '))
price_item = input('cena tovara za ed: ')

price_item_2 = int(price_item)
summa_item = kolvo_item * price_item_2
print('Obchay cena tovara:', summa_item) # Цена за общее количество товара

#Zadacha 2

min_urok = input('Введите кол-во минут до урока: ')
rast_puti = input('Введите растояние до школы: ')

vremy = int(rast_puti) / int(min_urok) # среднюю скорость находим 

print('Jon byl d puti ', vremy)

#Zadacha 3 
#parametry komnaty
shir_room = 3.0
vis_room = 2.4
dlina_room = 5.2

#razmery oboev
oboi_dlina = 10
oboi_shir = 0.5

plochad_room = (shir_room * dlina_room) * vis_room

plochad_room2 = round(plochad_room)

print('square ', plochad_room2) # opredelim plochad komnaty

oboi_dlina_2 = float(oboi_dlina)
oboi_plochad = oboi_dlina_2 * oboi_shir

print('rulon oboev ', oboi_plochad)











