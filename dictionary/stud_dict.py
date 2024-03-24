
# Создать словарь: студент и СЛОВАРЬ его оценок (дата - оценка)
# С помощью форматирования строк вывести табличку

stud_dict = {'stud1': 'Elena',
             'stud2': 'Ivan',
             'stud3': 'Max'
             }

stud_ocenk = {
    1002: '4',
    2302: '3',
    2602: '5',

}

two_dict = stud_dict | stud_ocenk # обьеденение двух словарей 
print(two_dict)
for item in two_dict:
    print(item)


table_column = []

for mark, data in two_dict.items():
    print(mark, data)

student_grades = {}

# Запрос оценок у студента
while True:
    grade = input("Введите оценку или 'end' для завершения: ")
    try:
        grade == 'end'

    except NameError:
        print('Цикл закончен')
    date = input("Введите дату получения оценки: ")
    student_grades[date] = grade

# Вывод таблицы оценок
for date, grade in student_grades.items():
    print(f"{date:<10} - {grade}")
print(date, grade)    