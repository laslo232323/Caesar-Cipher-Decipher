def decipher_eng():
    eng_lower = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(26):
        print()
        for c in text:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                f = eng_lower.find(c)
                if f + i < 26:
                    print(eng_lower[f + i], end='')
                else:
                    print(eng_lower[f + i - 26], end='')
            if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                f = eng_upper.find(c)
                if f + i < 26:
                    print(eng_upper[f + i], end='')
                else:
                    print(eng_upper[f + i - 26], end='')
            if c in '!@#$%^&*()-_+=}{[]\~`<>,./?}{: "':
                print(c, end='')            
        print()

def decipher_ukr():
    ukr_lower = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    ukr_upper = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    for i in range(33):
        print()
        for c in text:
            if c in 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя':
                f = ukr_lower.find(c)
                if f + i < 33:
                    print(ukr_lower[f + i], end='')
                else:
                    print(ukr_lower[f + i - 33], end='')
            if c in 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ':
                f = ukr_upper.find(c)
                if f + i < 33:
                    print(ukr_upper[f + i], end='')
                else:
                    print(ukr_upper[f + i - 33], end='')
            if c in '!@#$%^&*()-_+=}{[]\~`<>,./?}{: "':
                print(c, end='')            
        print()

def decipher_ru():
    ru_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    ru_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    for i in range(33):
        print()
        for c in text:
            if c in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
                f = ru_lower.find(c)
                if f + i < 33:
                    print(ru_lower[f + i], end='')
                else:
                    print(ru_lower[f + i - 33], end='')
            if c in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                f = ru_upper.find(c)
                if f + i < 33:
                    print(ru_upper[f + i], end='')
                else:
                    print(ru_upper[f + i - 33], end='')
            if c in '!@#$%^&*()-_+=}{[]\~`<>,./?}{: "':
                print(c, end='')            
        print()

flag = True
while flag != False: 
    language = (input('Choose your language, ua/eng/ru: '))
    flag = False

    if language == 'ua':
        more = 'так'
        while more == 'так':
            text = input('Введіть текст: ')
            decipher_ukr()
            print()
            more = input('Ще? так/ні/вибрати мову: ')
        if more == 'вибрати мову':
            flag = True
        while more != 'так' and more != 'ні' and more != 'вибрати мову':    
            more = input('Спробуй ще, так/ні/вибрати мову: ')
            if more == 'вибрати мову':
                flag = True

    if language == 'ru':
        more = 'да'
        while more == 'да':
            text = input('Введите свой текст на русском языке: ')
            decipher_ru()
            print()
            more = input('Еще? да/нет/выбрать язык: ')
        if more == 'выбрать язык':
            flag = True
        while more != 'да' and more != 'нет' and more != 'выбрать язык':    
            more = input('Попробуй еще, да/нет/выбрать язык: ')
            if more == 'выбрать язык':
                flag = True
                
    if language == 'eng':
        more = 'yes'
        while more == 'yes':
            text = input('Your text: ')
            decipher_eng()
            print()
            more = input('More? yes/no/language: ')
        if more == 'language':
            flag = True
        while more != 'yes' and more != 'no' and more != 'language':    
            more = input('Please try again, yes/no/language: ')
            if more == 'language':
                flag = True