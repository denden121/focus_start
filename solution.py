import os
import json
from car import Car

def check_car(id_car):
    '''проверка есть ли файл'''
    flag = False
    for i in list_cars:
        if i.split(';')[0] == id_car:
            flag = True
            break
    return flag


def print_menu():
    '''Вывод меню'''
    print('Нажмите 1 - Посмотреть сведения о автомобиле\n'
          + 'Нажмите 2 - Добавления нового автомобиля\n'
            + 'Нажмите 3 - Удаление автомобиля\n'
            + 'Нажмите 4 - Редактировать информацию об автомобиле\n'
            + 'Нажмите 5 - Просмотреть список автомобилей\n'
            + 'Нажмите 6 - Выход из программы')


def print_information_about_car(list_cars):
    '''Вывод информации о машине'''
    print("Введите идентификатор машины")
    id_car = input()
    for i in list_cars:
        i = i.split(';')
        if i[0] == id_car:
            print(' '.join(i[1:]))


def add_new_car(list_cars):
    '''Добавление новой машины'''
    print("Введите идентификатор машины (должен быть уникальным)")
    id_car = input()
    while True:
        if not check_car(id_car):
            break
        print("Идентификатор машины должен быть уникальным, повторите ввод")
        id_car = input()

    print("Введите производителя")
    manufacturer = input()
    print('Введите модель')
    model = input()
    print('Введите кузов')
    type_of_body = input()
    print('Введите год')
    year = input()
    list_cars.append(str(Car(id_car, manufacturer, model, type_of_body, year)))


def remove_car(list_cars):
    '''Удаление машины'''
    id_car = input("Введите идентификатор машины\n")
    for i in range(len(list_cars)):
        temp = list_cars[i].split(';')
        if temp[0] == id_car:
            del list_cars[i]
            print('Элемент успешно удален.')
            break
    print('Такой элемент не найден.')


def save_data(list_cars):
    '''Сохранение данных в файлы'''
    with open('list_car.txt', 'w') as f:
        for i in list_cars:
            f.write(i)


def edit_information_about_car(list_cars):
    '''Изменение данных о машине'''
    print('Введите идентификатор автомобиля который нужно редактировать')
    while True:
        id_car = input()
        if check_car(id_car):
            break
        print("Идентификатор машины должен не найден, повторите ввод")

    print('Введите чтобы вы хотели изменить(модель,производителя,кузов,год)')
    temp_car = ''
    for i in range(len(list_cars)):
        if list_cars[i].split(';')[0] == id_car:
            temp_car = list_cars[i]
            del list_cars[i]
            break
    temp_car = temp_car.split(';')
    while True:
        thing = input()
        if thing == 'модель':
            model = input('Введите модель ')
            temp_car[1] = model
            break
        elif thing == 'производитель':
            manufacturer = input('Введите производителя ')
            temp_car[2] = manufacturer
            break
        elif thing == 'кузов':
            body = input('Введите кузов ')
            temp_car[3] = body
            break
        elif thing == 'год':
            while True:
                year = input('Введите год ')
                if year.isdigit():
                    break
                print("Введен некорректный год, повторите ввод")
            temp_car[4] = year
            break
        else:
            print('Данные неверны. Повторите ввод')
    list_cars.append(';'.join(temp_car))
    print("Данные успешно сохранены")


def show_car(list_cars):
    '''Вывод всех автомобилей'''
    for i in list_cars:
        print(i.replace(';', '  '), end="")


def add_start_date():
    '''Добавление стартовых данных'''
    list_cars = list()
    if not os.path.exists("list_cars.txt"):
        with open('list_car.txt', 'w') as f:
            temp = Car('1', 'toyota', 'mark2', 'cidan', '2000')
            f.write(str(temp))
            list_cars.append(str(temp))
            temp = Car('2', 'toyota', 'chaser', 'cidan', '2000')
            f.write(str(temp))
            list_cars.append(str(temp))
            temp = Car('3', 'bmw', 'm5', 'jeep', '2018')
            f.write(str(temp))
            list_cars.append(str(temp))
            print('Это ваш первый запуск. Создано 3 машины')
    else:
        with open('list_car.txt') as f:
            list_cars = f.read().split('\n')
        try:
            del list_cars[-1]
            Car.num = list_cars[-1][0]
        except Exception:
            Car.num = 0
    return list_cars


list_cars = add_start_date()
print('Добрый день выберите что вы хотите сделать:\n')
while True:
    print_menu()
    command = input()
    if command == '1':
        print_information_about_car(list_cars)
    elif command == '2':
        add_new_car(list_cars)
    elif command == '3':
        remove_car(list_cars)
    elif command == '4':
        edit_information_about_car(list_cars)
    elif command == '5':
        show_car(list_cars)
    elif command == '6':
        print("До свидания")
        save_data(list_cars)
        break
    else:
        print("Введенные данные не верны повторите ввод")
