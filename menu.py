from utils import Logic

class Menu_base:
    """Main menu"""

    """Menu where you chose cipher or decipher"""
    def cipher_decipher_menu():
        global cipher_decipher
        cipher_decipher = input('Cipher[1]/Decipher[2]: ')
        Menu_base.language_input()

    """Menu where you chose your language main menu, and space work of cipher/decipher"""
    def language_input():
        global language
        language = (input('Ua[1]/Eng[2]/Ru[3]: '))
        Menu_base.menu()

    """Main menu on your language"""
    def menu():
        """1 = cipher, 2 = decipher"""
        if cipher_decipher == '1' or '2':
            """Russian cipher start and end menu"""
            if language == '3' and cipher_decipher == '1':
                more = '1'
                while more == '1':
                    print('Добро пожаловать в шифр Цезаря!')
                    Logic.ru_data()
                    more = input('Еще? да[1]/выход[2]/меню[3]: ')
                    if more == '3':
                        Menu_base.cipher_decipher_menu()
                    if more == '2':
                        Menu_base.exit()
                    while more != '1' and more != '2' and more != '3':
                        more = input('Попробуй еще, да[1]/выход[2]/меню[3]: ')
                    if more == '1':
                        Menu_base.menu()
            """Ukrainian cipher start and end menu"""
            if language == '1' and cipher_decipher == '1':
                more = '1'
                while more == '1':
                    print('Вітаю, ласкаво просимо до шифру Цезаря!')
                    Logic.ua_data()
                    more = input('Ще? так[1]/завершити[2]/меню[3]: ')
                    if more == '3':
                        Menu_base.cipher_decipher_menu()
                    if more == '2':
                        Menu_base.exit()
                    while more != '1' and more != '2' and more != '3':
                        more = input('Спробуй ще, так[1]/завершити[2]/меню[3]: ')
                    if more == '1':
                        Menu_base.menu()
            """English cipher start and end menu"""
            if language == '2' and cipher_decipher == '1':
                more = '1'
                while more == '1':
                    print('Hey! Welcome to the Caesar Cipher.')
                    Logic.eng_data()
                    more = input('More? yes[1]/exit[2]/menu[3]: ')
                    if more == '3':
                        Menu_base.cipher_decipher_menu()
                    if more == '2':
                        Menu_base.exit()
                    while more != '1' and more != '2' and more != '3':
                        more = input('Please try again, yes[1]/exit[2]/menu[3]: ')
                    if more == '1':
                        Menu_base.menu()

            """Ukrainian decipher start and end menu"""
            if language == '1' and cipher_decipher == '2':
                more = '1'
                while more == '1':
                    print('Вітаю, ласкаво просимо до дешифратора Цезаря!')
                    Logic.ua_data_de()
                    more = input('Ще? так[1]/завершити[2]/меню[3]: ')
                    if more == '3':
                        Menu_base.cipher_decipher_menu()
                    if more == '2':
                        Menu_base.exit()
                    while more != '1' and more != '2' and more != '3':
                        more = input('Спробуй ще, так[1]/завершити[2]/меню[3]: ')
                    if more == '1':
                        Menu_base.menu()
            """English decipher start and end menu"""
            if language == '2' and cipher_decipher == '2':
                more = '1'
                while more == '1':
                    print('Hey! Welcome to the Caesar Decipher.')
                    Logic.eng_data_de()
                    more = input('More? yes[1]/exit[2]/menu[3]: ')
                    if more == '3':
                        Menu_base.cipher_decipher_menu()
                    if more == '2':
                        Menu_base.exit()
                    while more != '1' and more != '2' and more != '3':
                        more = input('Спробуй ще, так[1]/завершити[2]/меню[3]: ')
                    if more == '1':
                        Menu_base.menu()
            """Russian decipher start and end menu"""
            if language == '3' and cipher_decipher == '2':
                more = '1'
                while more == '1':
                    print('Добро пожаловать в дешифратор Цезаря!')
                    Logic.ru_data_de()
                    more = input('Еще? да[1]/выход[2]/меню[3]: ')
                    if more == '3':
                        Menu_base.cipher_decipher_menu()
                    if more == '2':
                        Menu_base.exit()
                    while more != '1' and more != '2' and more != '3':
                        more = input('Спробуй ще, так[1]/завершити[2]/меню[3]: ')
                    if more == '1':
                        Menu_base.menu()

    """Exit program"""
    def exit():
        """Farewell text depending on the selected language"""
        if language == '2':
            print('Good bye!')
        if language == '3':
            print('Пока!')
        if language == '1':
            print('До побачення!')
        raise SystemExit


# Start program
Menu_base.cipher_decipher_menu()