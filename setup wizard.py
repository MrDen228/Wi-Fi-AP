import os
from time import sleep

print ('Hello, please select your language.')
print ('1 - ru')
print ('2 - en')
lang = input ('Enter the namber:')

#ru
if lang == "1":
    print ('Меню:')
    print ('1 - запуск отрибутов (рекомендуется в первый раз)')
    print ('2 - У меня не работает')
    print ('3 - Настройки')
    menu1 = input ('Введите номер: ')
    if menu1 == "1":
        user = input ('Введите имя вашего пользователя. Посмотреть его можно тут (C:/users): ')
        print ('Открываю файл...')
        os.system('call C:/users/' + user + '/Downloads/Wi-Fi-AP/wi-fi.bat')
        print ('Навание вашей точки дступа: My Wi-Fi')
        print ('Пароль вашей точки доступа: 1234567890')
        print ('Перед тем как нажать кнопку "Настройки" проверьте работаспособость вашего Wi-Fi (нажмите на файл "access point master.py")')
        print ('Если у вас появились какие-то проблемы, то в меню выберите "У меня не работает Wi-Fi"')
        print ('Хорошего дня!')
    elif menu1 == "2":
        print ('Если ваша точка доступа не работает, то скорее всего был указан неверный путь.')
        print ('В данном случае вам прийдётся ввести его вручную.')
        print ('В поиске найдите файл "wi-fi.bat" и скопируйте его путь')
        go = input ('Введите путь сюда (Пример: С:/users/(ваше имя пользователя)/desktop/wi-fi.bat: ')
        print ('Запускаю повторный запуск файла...')
        os.system(go)
        print ('Если точка доступа опять не работает, то возможно вы опять не правильно указали путь. Если вы правельно ввели путь, то возможно дело в версии Windows. Она должна быть 7, 8 ,10.')
        print ('Если у вас всё заработало, то вы можете переходить к пункту настройка.')
    elif menu1 == "3":
        print ('Если вы выбрали данный пункт, то скорее всего у вас всё работает.')
        print ('Что бы поменять пораметры вашей точки доступа нажмите на файл "wi-fi.bat" ПКМ и выберите пункт изменить')
        print ('В появившемся окне найдите пункт ssid (он отвечает за имя вашей точки доступа) и пункт key (это пароль) и измените их на свои значения')
        print ('Затем запустите этот файл заново, нажав на него два раза ЛКМ.')
    else:
        print ('Вы неверно ввели номер!')



# en
elif lang == "2":
    print ('Menu:')
    print ('1 - launch attributes (recommended for the first time)')
    print ('2 - It does not work for me')
    print ('3 - Settings')
    menu1 = input ('Enter number: ')
    if menu1 == "1":
        user = input ('Enter your username. You can see it here (C: / users): ')
        print ('I open the file ...')
        os.system('call C:/users/' + user + '/Downloads/Wi-Fi-AP/wi-fi.bat')
        print ('Pointing your point of access: My Wi-Fi')
        print ('Your access point password: 1234567890')
        print ('Before clicking the "Settings" button, check the working ability of your Wi-Fi (click on the file "access point master.py")')
        print ('If you have any problems, then select "It does not work for me" in the menu')
        print ('Have a nice day!')
    elif menu1 == "2":
        print ('If your access point does not work, then most likely the wrong path was specified.')
        print ('In this case, you will have to enter it manually.')
        print ('In the search, find the file "wi-fi.bat" and copy its path')
        go = input ('Enter the path here (Example: C: / users / (your username) /desktop/wi-fi.bat: ')
        print ('I start re-launching the file ...')
        os.system(go)
        print ('If the access point does not work again, then maybe you again did not correctly specify the path. If you entered the path correctly, then it may be the case in the Windows version. It should be 7, 8, 10.')
        print ('If everything worked for you, then you can go to the setup item.')
    elif menu1 == "3":
        print ('If you selected this item, then most likely everything works for you.')
        print ('To change the settings of your access point, click on the file "wi-fi.bat" Right mouse button and select the edit item')
        print ('In the window that appears, find the ssid item (it is responsible for the name of your access point) and the key item (this is the password) and change them to your values')
        print ('Then run this file again by double-clicking on it with left mouse button.')
    else:
        print ('You entered the number incorrectly!')


#no
else:
    print ('You entered the number incorrectly!')

    

