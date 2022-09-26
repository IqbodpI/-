from random import *

print('Программа создания паролей')

# Вводимые пользователем аргументы
user_data = []
# Вопросы пользователю
questions = ['Количество паролей: ', 'Длина пароля: ', 'Включить в пароль цифры? д = Да, н = Нет: ', 'Включить в пароль заглавные буквы латиницы? д = Да, н = Нет: ', 'Включить в пароль строчные буквы латиницы? д = Да, н = Нет: ', 'Включить в пароль спец. символы? д = Да, н = Нет: ', 'Исключить из пароля неоднозначные символы I1lO0? д = Да, н = Нет: ', 'Использовать разделитель? д = Да, н = Нет: ', 'Через сколько символов вставлять разделитель?: ']
# Строки различных символов
list_ = ['0123456789', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '~`!@#$%^&*()_-+=,./<>?;:\'\"\\|[{]}']
# Неоднозначные символы
ambig = ['I1lO0']
# Списки выбранных пользователем символов
chars = []

# Запрос на продолжение или закрытие программы
def ask():
    user_a = input('\nХотите сформировать новый список паролей? д = Да. другая клавиша = Выход: ')
    if user_a == 'l' or user_a == 'д': user_param()
    else: 
        print('Завершение работы')
        exit(0)


# Проверка на корректность введённых пользователем численных данных
def valid_d(digit, i):
    temp = False
    while temp == False:
        if digit.isdigit():
            user_data.append(digit)
            return True
        else:
            print('Некорректный ввод')
            digit = input(questions[i])

# Проверка на корректность введённых пользователем строковых данных
def valid_c(char, i):
    temp = False
    while temp == False:
        if char in ('lyдн'):
            user_data.append(char)

            # Формирование списков из одобренных пользователем символов
            if char in ('lд') and i < 6: chars.append(list_[i - 2])
            return True
        else:
            print('Некорректный ввод')
            char = input(questions[i])    
    
# сбор аргументов от пользователя
def user_param():
    for i in range(9):
        temp = input(questions[i])
        if (2 > i or i > 7) and valid_d(temp, i): continue
        elif (1 < i or i < 8) and valid_c(temp, i): continue

    # Проверка на используемые строки в формировании паролей
    if len([i for i in range(2,6) if user_data[i] in ('нy')]) == 4:
        print('\nВы не выбрали ни одного варианта для формирования паролей\n')
        ask()
        
    generate_password()

# Генератор паролей
def generate_password():
    # Проверка указывал ли пользователь, и если указывал, удаление неоднозначных символов
    if user_data[6] in ('lд'):
        for _ in range(len(chars)):
            for i in chars[_]:
                if i in ambig: chars.replace(i, '')
        
    # Формирование паролей
    for _ in range(int(user_data[0])):
        temp = []
        for i in range(1, int(user_data[1]) + 1): temp.append(choice(chars[i % len(chars)]))

        # Перемешивание символов пароля в случайном порядке
        shuffle(temp)
        temp = ''.join(temp)
        
        # Проверка указывал ли пользователь, и если указывал, дробление паролей знаком тире через указанное пользователем количество символов
        step = int(user_data[8])
        print('-'.join(temp[i:i + step] for i in range(0, len(temp), step)) if user_data[7] in ('lд') else print(temp))
    
    ask()

user_param()
