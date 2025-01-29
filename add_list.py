#Запрашиваем у пользователя информацию для создания заметки
from add_input import titles
from tren import username, content, status, created_date, issue_date

username=input("Введите имя пользователя: ")
content=input("Введите описание заметки: ")
status=input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date=input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date=input("Ведите дату истечения заметки в формате 'день-месяц-год': ")

#Создаем список заголовков заметки
titles=[]
for i in range(3):
    title=input(f"Введите загодовок заметки {i+1}: ")
    titles.append(title)

#Выводим все данные заметки
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовки заметки: ", titles)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", issue_date)