from random import randint

x = randint (0,100)
print("Number is", x)
a = '''_/﹋\_
(҂`_´)
<,︻╦╤─ ҉ - -
_/﹋\_'''
b = '''█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█'''
c = '''╔══╗
║██║
║(O)║♫ ♪ ♫ ♪
╚══╝
▄ █ ▄ █ ▄ ▄ █ ▄ █ ▄ █
Min- - - - - - - - - - - -●Max'''

if x < 30:
    print(a)
elif x < 60:
    print(b)
else:
    print(c)