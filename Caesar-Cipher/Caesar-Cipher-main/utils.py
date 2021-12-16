

class Logic():
    """Логика программы"""

    def change_word_eng(text, side_shift, number_shift):
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

    def change_word_ua(text, side_shift, number_shift):
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

    def change_word_ru(text, side_shift, number_shift):
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