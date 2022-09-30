from random import *

print('Программа создания паролей')

# Вводимые пользователем аргументы
user_data = []

# Списки выбранных пользователем символов
chars = []

# Запрос на продолжение или закрытие программы
def ask():
    user_a = input('\nХотите сформировать новый список паролей? д = Да. другая клавиша = Выход: ')
    if user_a in ('lдДL'): user_param()
    else: 
        print('Завершение работы')
        exit(0)

# сбор аргументов от пользователя
def user_param():
    
    # Вопросы пользователю
    questions = ['Количество паролей: ', 'Длина пароля: ', 'Включить в пароль цифры? д = Да, н = Нет: ', 'Включить в пароль заглавные буквы латиницы? д = Да, н = Нет: ', 'Включить в пароль строчные буквы латиницы? д = Да, н = Нет: ', 'Включить в пароль спец. символы? д = Да, н = Нет: ', 'Исключить из пароля неоднозначные символы \"01IlO\"? д = Да, н = Нет: ', 'Использовать разделитель? д = Да, н = Нет: ', 'Через сколько символов вставлять разделитель?: ']
    # Строки различных символов
    list_ = ['0123456789', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz', '~`!@#$%^&*()_-+=,./<>?;:\'\"\\|[{]}']    
    
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
            if char in ('lyднДНLY'):
                user_data.append(char)
    
                # Формирование списков из одобренных пользователем символов
                if char in ('lдLД') and i < 6: chars.append(list_[i - 2])
                return True
            else:
                print('Некорректный ввод')
                char = input(questions[i])    
                
    for i in range(8):
        temp = input(questions[i])
        if 2 > i and valid_d(temp, i): continue
        elif 1 < i and valid_c(temp, i): continue

    if user_data[7] in ('lдLД'):
        temp = input(questions[8])
        if valid_d(temp, 8): print('')

    # Проверка на используемые строки в формировании паролей
    if len([i for i in range(2,6) if user_data[i] in ('нyYН')]) == 4:
        print('\nВы не выбрали ни одного варианта для формирования паролей\n')
        ask()
        
    generate_password()

# Генератор паролей
def generate_password():
    # Неоднозначные символы
    ambig = ['01', 'IO', 'l']

    # Проверка указывал ли пользователь, и если указывал, удаление неоднозначных символов
    if user_data[6] in ('lдДL'):
        for _ in range(len(chars)):
            for i in ambig[_]: chars[_] = chars[_].replace(i, '')
        
    # Формирование паролей
    for _ in range(int(user_data[0])):
        temp = []
        for i in range(1, int(user_data[1]) + 1): temp.append(choice(chars[i % len(chars)]))

        # Перемешивание символов пароля в случайном порядке
        shuffle(temp)
        temp = ''.join(temp)

        # Проверка указывал ли пользователь, и если указывал, дробление паролей знаком тире через указанное пользователем количество символов
        if user_data[7] in ('lдLД'):
            step = int(user_data[8])
            print('-'.join(temp[i:i + step] for i in range(0, len(temp), step)))
        else: print(temp)

    ask()

user_param()
