from languages import Language
from utils import Logic

# MENU
flag = True
while flag != False:
    language = (input('Choose your language, ua/eng/ru: '))
    flag = False

if language == 'ru':
    Language.ru()

if language == 'ua':
    Language.ua()

if language == 'eng':
    Language.eng()