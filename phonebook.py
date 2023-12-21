# 1. Я не понял изначально в какой момент программа должна выгружать данные обратно в ТХТ и сделал что при нажатии 7 программа делает выгрузку файла и остановку цикла
# 2. К сожалению не доработал ее полноценно, в ТХТ изначально убрал лишние символы(пробелы) чтобы не пришлось их фильтровать и обрезать, так как в описании они допускаются, но перенос строки убрал через replace с заменой \n на ''
# 3. Так же понимаю что не делал ничего с регистром, по этому при поиске человека или внесении данных это нужно учитывать
# 4. исходя из пункта 2, в пункт 6 добавлял данные абонента через запятую без пробелов


# Вызов меню
def show_menu():
    print('',
          '1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Изменить номер телефона',
          '4. Удалить запись',
          '5. Найти абонена по номеру телефона',
          '6. Добавить абонента в справочник',
          '7. Закончить работу', 
          '', sep = '\n')
    choice = int(input("Выберите нужный пункт меню: "))
    return choice

# главное обращение
def work_with_phonebook():
    choice = show_menu()

    phone_book = read_txt('phonebook.txt')

    while (choice):

        if choice==1:
            print(phone_book)
        elif choice==2:
            last_name=input('Введите Фамилию: ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('Введите Фамилию: ')
            new_number=input('Новый номер: ')
            print(change_number(phone_book,last_name,new_number))
        elif choice==4:
            last_name=input('Введите Фамилию: ')
            print(delete_by_lastname(phone_book,last_name))
        elif choice==5:
            number=input('Введите номер телефона: ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('Введите Фамилию, Имя, Телефон и описание через запятую: ')
            add_user(phone_book,user_data)
        elif choice==7:
            write_txt('phonebook.txt',phone_book)
            break
        choice = show_menu()


# Чтение файла из txt
def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            record = {k: v.replace('\n', '') for k, v in record.items()}
            phone_book.append(record)

        return phone_book

# Запись файла обратно из списка
def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s += str(v) + ','
            phout.write(f'{s[:-1]}\n')

# Найти телефон по фамилии
def find_by_lastname(phone_book, last_name):
    for i in phone_book:
        if i['Фамилия'] == last_name:
            return f'Фамилия {last_name} - телефон {i['Телефон']}'
    else:
        return 'Такая Фамилия не найдена'


# Изменить номер телефона
def change_number(phone_book,last_name,new_number):
    for i in phone_book:
        if i['Фамилия'] == last_name:
            i['Телефон'] = new_number
        return 'Номер обновлен'



# Удалить запись
def delete_by_lastname(phone_book,last_name):
    for i in phone_book:
        if i['Фамилия'] == last_name:
            phone_book.remove(i)
            return 'Запись удалена'
              
    else:
        return 'Такая Фамилия не найдена'

# Найти абонена по номеру телефона    
def find_by_number(phone_book,number):
    for i in phone_book:
        if i['Телефон'] == number:
            return f'Телефон {number} пренаджелит {i['Фамилия']} {i['Имя']}'
    else:
        return 'Такой телефон не найден'



# Добавить абонента в справчник
def add_user(phone_book,user_data):
    values_list = user_data.split(',')
    person = {
        'Фамилия' : str(values_list[0]),
        'Имя' : str(values_list[1]),
        'Телефон' : int(values_list[2]),
        'Описание' : str(values_list[3])
    }
    phone_book.append(person)
    print('Данные внесены')




work_with_phonebook()