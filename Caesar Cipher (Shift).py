def change_word_eng():
    if side_shift == 'right' or side_shift == 'Right':
        for c in text:
            flag = False
            if c in 'abcdefghijklmnopqrstuvwxyz':
                if ord(c) + number_shift > 122:
                    if ord(c) + number_shift - 26 <= 122:
                        print(chr(ord(c) + number_shift - 26), end='')
                        flag = True
                    else:
                        print(chr(ord(c) + number_shift - 26 - 26), end='')
                        flag = True
                if flag == False:
                    print(chr(ord(c) + number_shift), end='')
            if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                if ord(c) + number_shift > 90 and ord(c) + number_shift < 97 + number_shift:
                    if ord(c) + number_shift - 26 <= 90:
                        print(chr(ord(c) + number_shift - 26), end='')
                        flag = True
                    else:
                        print(chr(ord(c) + number_shift - 26 - 26), end='')
                        flag = True
                if flag == False:
                    print(chr(ord(c) + number_shift), end='')
            if c in '!@#$%^&*()-_+=}{[]\~`<>,./?}{: "':
                print(c, end='')            

    if side_shift == 'left' or side_shift == 'Left':
        for c in text:
            flag = False
            if c in 'abcdefghijklmnopqrstuvwxyz':
                if ord(c) - number_shift <= 97:
                    if ord(c) - number_shift + 26 > 122:
                        print(chr(ord(c) - number_shift + 26 - 26), end='')
                        flag = True
                    else:
                        print(chr(ord(c) - number_shift + 26), end='')
                        flag = True
                if flag == False:
                    print(chr(ord(c) - number_shift), end='')
            if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                if ord(c) - number_shift <= 65:
                    if ord(c) - number_shift + 26 > 90:
                        print(chr(ord(c) - number_shift + 26 - 26), end='')
                        flag = True
                    else:
                        print(chr(ord(c) - number_shift + 26), end='')
                        flag = True
                if flag == False:
                    print(chr(ord(c) - number_shift), end='')
            if c in '!@#$%^&*()-_+=}{[]\~`<>,./?}{: "':
                print(c, end='')

def change_word_ua():
    ukr_lower = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    ukr_upper = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    if side_shift == 'вправо' or side_shift == 'Вправо':
        for c in text:
            flag = False
            if c in 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя':
                f = ukr_lower.find(c)
                if f + number_shift < 33:
                    print(ukr_lower[f + number_shift], end='')
                else:
                    print(ukr_lower[f + number_shift - 33], end='')
            if c in 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ':
                f = ukr_upper.find(c)
                if f + number_shift < 33:
                    print(ukr_upper[f + number_shift], end='')
                else:
                    print(ukr_upper[f + number_shift - 33], end='')
            if c in '!@#$%^&*()-_+=}{[]\~`<>,./?}{: "':
                print(c, end='')

    if side_shift == 'вліво' or side_shift == 'Вліво':
        for c in text:
            flag = False
            if c in 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя':
                f = ukr_lower.find(c)
                if f - number_shift < 33:
                    print(ukr_lower[f - number_shift], end='')
                else:
                    print(ukr_lower[f - number_shift + 33], end='')
            if c in 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ':
                f = ukr_upper.find(c)
                if f - number_shift < 33:
                    print(ukr_upper[f - number_shift], end='')
                else:
                    print(ukr_upper[f - number_shift + 33], end='')
            if c in '!@#$%^&*()-_+=}{[]\~`<>,./?}{: "':
                print(c, end='')

def change_word_ru():
    ru_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    ru_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    if side_shift == 'право' or side_shift == 'Право':
        for c in text:
            flag = False
            if c in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
                f = ru_lower.find(c)
                if f + number_shift < 33:
                    print(ru_lower[f + number_shift], end='')
                else:
                    print(ru_lower[f + number_shift - 33], end='')
            if c in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                f = ru_upper.find(c)
                if f + number_shift < 33:
                    print(ru_upper[f + number_shift], end='')
                else:
                    print(ru_upper[f + number_shift - 33], end='')
            if c in '!@#$%^&*()-_+=}{[]\~`<>,./?}{: "':
                print(c, end='')

    if side_shift == 'лево' or side_shift == 'Лево':
        for c in text:
            flag = False
            if c in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
                f = ru_lower.find(c)
                if f - number_shift < 33:
                    print(ru_lower[f - number_shift], end='')
                else:
                    print(ru_lower[f - number_shift + 33], end='')
            if c in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                f = ru_upper.find(c)
                if f - number_shift < 33:
                    print(ru_upper[f - number_shift], end='')
                else:
                    print(ru_upper[f - number_shift + 33], end='')
            if c in '!@#$%^&*()-_+=}{[]\~`<>,./?}{: "':
                print(c, end='')

flag = True
while flag != False: 
    language = (input('Choose your language, ua/eng/ru: '))
    flag = False

    if language == 'ua':
        more = 'так'
        count = 0
        while more == 'так':
            if count > 0:
                print('Вітаю, ласкаво просимо до шифру Цезаря!', 'Ще xD ' * count)
            else:
                print('Вітаю, ласкаво просимо до шифру Цезаря!')
            text = input('Введіть ваш текст українською: ')
            side_shift = input('Вибери бік зсуву, вліво/вправо: ')
            while side_shift != 'вліво' and side_shift != 'Вліво' and side_shift != 'вправо' and side_shift != 'Вправо':
                side_shift = input('Спробуй ще, вліво/вправо: ')
            number_shift = int(input('Вибери цифру зсуву від 1 до 25: '))
            while 1 < number_shift > 25:
                number_shift = int(input('Спробуй ще, твоя цифра повинна бути від 1 до 25: '))
            more = 'стоп'
            count += 1
    
            print('Твій шифр Цезаря: ', end='')
            change_word_ua()
            print()
            more = input('Ще? так/ні/вибрати мову: ')
            if more == 'вибрати мову':
                flag = True
            while more != 'так' and more != 'ні' and more != 'вибрати мову':    
                more = input('Спробуй ще, так/ні/вибрати мову: ')
                if more == 'вибрати мову':
                    flag = True
    
    if language == 'eng':
        more = 'yes'
        count = 0
        while more == 'yes':
            if count > 0:
                print('Hey! Welcome to the Caesar Cipher.', 'Again xD ' * count)
            else:
                print('Hey! Welcome to the Caesar Cipher.')
            text = input('Your text: ')
            side_shift = input('Choose your side to shift, left/right: ')
            while side_shift != 'left' and side_shift != 'Left' and side_shift != 'right' and side_shift != 'Right':
                side_shift = input('Please try again, left/right: ')
            number_shift = int(input('Choose your shift from 1 to 25: '))
            while 1 < number_shift > 25:
                number_shift = int(input('Please try again, your shift should be 1 to 25: '))
            more = 'no'
            count += 1
    
            print('Your Caesar Cipher: ', end='')
            change_word_eng()
            print()
            more = input('More? yes/no/language: ')
            if more == 'language':
                flag = True
            while more != 'yes' and more != 'no' and more != 'language':
                more = input('Please try again, yes/no/language: ')
                if more == 'language':
                    flag = True
                    
    if language == 'ru':
        more = 'да'
        count = 0
        while more == 'да':
            if count > 0:
                print('Привет, добро пожаловать в шифр Цезаря!', 'Еще xD ' * count)
            else:
                print('Привет, добро пожаловать в шифр Цезаря!')
            text = input('Введите свой текст на русском языке: ')
            side_shift = input('Выберите сторону сдвига, лево/право: ')
            while side_shift != 'лево' and side_shift != 'Лево' and side_shift != 'право' and side_shift != 'Право':
                side_shift = input('Попробуй еще, лево/право: ')
            number_shift = int(input('Выбери цифру сдвига от 1 до 25: '))
            while 1 < number_shift > 25:
                number_shift = int(input('Попробуй еще, твоя цифра должна быть от 1 до 25: '))
            more = 'стоп'
            count += 1
    
            print('Твой шифр Цезаря: ', end='')
            change_word_ru()
            print()
            more = input('Еще? да/нет/выбрать язык: ')
            if more == 'выбрать язык':
                flag = True
            while more != 'да' and more != 'нет' and more != 'выбрать язык':    
                more = input('Попробуй еще, да/нет/выбрать язык: ')
                if more == 'выбрать язык':
                    flag = True
