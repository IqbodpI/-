from random import randint as ri

print('Добро пожаловать в числовую угадайку!')

def ask():
    inp = input('Сыграем ещё? д = ДА!, любая другая клавиша = Выход: ')
    if inp == 'д' or inp == 'l': random()
    else:
        print('Пока!')
        exit(0)

def input_data():
    temp = True
    while temp == True:
        i_d = input('Введите число от 1 до 100: ')
        if i_d.isdigit():
            if 0 < int(i_d) < 101: 
                    temp = False
                    return int(i_d)
        else: print('Некорректный ввод')

def game(random_number, number_attempts):
    attempts_left = 0

    while attempts_left < number_attempts:
        data = input_data()
        attempts_left += 1
        if data == random_number:
            print('Поздравляю, вы угадали!\n', 'Потраченных попыток', attempts_left)
            ask()
        elif data > random_number: print('Ваше число больше загаданного, попробуйте еще разок')
        else: print('Ваше число меньше загаданного, попробуйте еще разок')
        
    print('К сожалению вы истратили все попытки и проиграли')
    print('Я загадал:', random_number)
    ask()

def random():
    random_number, number_attempts = ri(1, 100), 1
    attempts = random_number
    
    while attempts > 2:
        attempts /= 2
        number_attempts += 1
    print('Угадайте загаданное число.\n', 'Количество попыток', number_attempts)
    game(random_number, number_attempts)

random()
