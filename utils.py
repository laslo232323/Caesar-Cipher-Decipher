class Logic:
    """Utils"""

    """Cipher"""
    def change_word_eng(text, side_shift, number_shift):
        """Logic cipher english text"""
        if side_shift == '2':
            for c in text:
                flag = False
                """Small case"""
                if c in 'abcdefghijklmnopqrstuvwxyz':
                    """Side shift right"""
                    if ord(c) + number_shift > 122:
                        if ord(c) + number_shift - 26 <= 122:
                            print(chr(ord(c) + number_shift - 26), end='')
                            flag = True
                        else:
                            print(chr(ord(c) + number_shift - 26 - 26), end='')
                            flag = True
                    if flag == False:
                        print(chr(ord(c) + number_shift), end='')
                """large case"""
                if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    """Side shift right"""
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

        if side_shift == '1':
            for c in text:
                flag = False
                """Small case"""
                if c in 'abcdefghijklmnopqrstuvwxyz':
                    """Side shift right"""
                    if ord(c) - number_shift <= 97:
                        if ord(c) - number_shift + 26 > 122:
                            print(chr(ord(c) - number_shift + 26 - 26), end='')
                            flag = True
                        else:
                            print(chr(ord(c) - number_shift + 26), end='')
                            flag = True
                    if flag == False:
                        print(chr(ord(c) - number_shift), end='')
                """large case"""
                if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    """Side shift right"""
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

    def change_word_ua(text, side_shift, number_shift):
        """Logic cipher ukrainian text"""
        ukr_lower = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
        ukr_upper = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
        if side_shift == '2':
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

        if side_shift == '1':
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

    def change_word_ru(text, side_shift, number_shift):
        """Logic cipher russian text"""
        ru_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        ru_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        if side_shift == '2':
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

        if side_shift == '1':
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
    """Cipher"""

    """Decipher"""
    def decipher_eng(text):
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

    def decipher_ukr(text):
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

    def decipher_ru(text):
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
    """Decipher"""

    """Data cipher"""
    def eng_data():
        text = input('Your text: ')
        side_shift = input('Choose your side to shift, left[1]/right[2]: ')
        while side_shift != '1' and side_shift != '2':
            side_shift = input('Please try again, left[1]/right[2]: ')
        number_shift = int(input('Choose your shift from 1 to 25: '))
        while 1 < number_shift > 25:
            number_shift = int(input('Please try again, your shift should be 1 to 25: '))
        print('Your Caesar Cipher: ', end='')
        Logic.change_word_eng(text, side_shift, number_shift)
        print()

    def ru_data():
        text = input('Введите свой текст на русском языке: ')
        side_shift = input('Выберите сторону сдвига, лево[1]/право[2]: ')
        while side_shift != '1' and side_shift != '2':
            side_shift = input('Попробуй еще, лево[1]/право[2]: ')
        number_shift = int(input('Выбери цифру сдвига от 1 до 25: '))
        while 1 < number_shift > 25:
            number_shift = int(input('Попробуй еще, твоя цифра должна быть от 1 до 25: '))
        print('Твой шифр Цезаря: ', end='')
        Logic.change_word_ru(text, side_shift, number_shift)
        print()

    def ua_data():
        text = input('Введіть ваш текст українською: ')
        side_shift = input('Вибери бік зсуву, вліво[1]/вправо[2]: ')
        while side_shift != '1' and side_shift != '2':
            side_shift = input('Спробуй ще, вліво[1]/вправо[2]: ')
        number_shift = int(input('Вибери цифру зсуву від 1 до 25: '))
        while 1 < number_shift > 25:
            number_shift = int(input('Спробуй ще, твоя цифра повинна бути від 1 до 25: '))
        print('Твій шифр Цезаря: ', end='')
        Logic.change_word_ua(text, side_shift, number_shift)
        print()
    """Data cipher"""

    """Data decipher"""
    def ua_data_de():
        text = input('Введіть зашифрований текст: ')
        Logic.decipher_ukr(text)
        print()

    def ru_data_de():
        text = input('Введите зашифрованный текст на русском языке: ')
        Logic.decipher_ru(text)
        print()

    def eng_data_de():
        text = input('Your cipher text: ')
        Logic.decipher_eng(text)
        print()
    """Data decipher"""