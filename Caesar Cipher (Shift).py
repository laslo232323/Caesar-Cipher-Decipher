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

more = 'y'
while more == 'y':
    print('Hey! Welcome to the Caesar Cipher.')
    text = input('Your text: ')
    side_shift = input('Choose your side to shift, left/right: ')
    while side_shift != 'left' and side_shift != 'Left' and side_shift != 'right' and side_shift != 'Right':
        side_shift = input('Please try again, left/right: ')
    number_shift = int(input('Choose your shift from 1 to 25: '))
    while 1 < number_shift > 25:
        number_shift = int(input('Please try again, your shift should be 1 to 25: '))
    more = 'n'
    
    print('Your Caesar Cipher: ', end='')
    change_word_eng()
    print()
    more = input('More? y/n: ')
