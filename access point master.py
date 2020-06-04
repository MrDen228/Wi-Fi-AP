import os
from time import sleep

print ('Hello, please select your language.')
print ('1 - ru')
print ('2 - en')
lang = input ('Enter the number:')


#ru
if lang == "1":
    print ('Здравсвуйте, вас приветствует мастер по созданию точки доступа вай фай на Windows.')
    print ('1 - запуск')
    print ('2 - выключение')
    print ('3 - перезапуск')
    a1 = input ('Выберите действие которое вы хотите:')
    if a1 == '1':
        print ('Запускаю точку доступа')
        sleep(0.5)
        os.system ('netsh wlan start hostednetwork')
        print ('точка доступа успешно запущена!')
    elif a1 == "2":
        print ('Выключаю точку доступа')
        sleep(0.5)
        os.system ('netsh wlan stop hostednetwork')
        print ('точка доступа успешо выключена!')
    elif a1 == "3":
        print ('Перезапускаю точку доступа')
        sleep(0.5)
        os.system ('netsh wlan stop hostednetwork')
        sleep(2)
        os.system ('netsh wlan start hostednetwork')
        print ('Точка доступа успешно перезапущена')
    else:
        print ('Я не понимаю, что вы ввели')


#en
elif lang == "2":
    print ('Hello, you are welcomed by the wizard on creating a Wi-Fi access point on Windows.')
    print ('1 - Launch')
    print ('2 - Shutdown')
    print ('3 - Restart')
    a2 = input ('Choose the action you want:')
    if a2 == '1':
        print ('I launch the access point')
        sleep(0.5)
        os.system ('netsh wlan start hostednetwork')
        print ('Access Point Launched Successfully!')
    elif a2 == "2":
        print ('I turn off the access point')
        sleep(0.5)
        os.system ('netsh wlan stop hostednetwork')
        print ('access point turned off successfully!')
    elif a1 == "3":
        print ('Restarting access point')
        sleep(0.5)
        os.system ('netsh wlan stop hostednetwork')
        sleep(2)
        os.system ('netsh wlan start hostednetwork')
        print ('Access Point Restarted Successfully')
    else:
        print ('I do not understand what you entered.')

# if entered incorrectly.
else:
    print ('I do not understand what you entered.')



