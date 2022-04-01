import time
import os
from datetime import datetime

def creator():
    text_bot()
    print('\033[1;31mEsse programa foi criado por {}\033[m'.format('\033[1;36;41mCleverson.\033[m'))
    print("\033[1;31m\nAperte a tecla \033[1;33m{}\033[m \033[1;31mpara sair.\033[m\033[m".format("[Enter]"))
    finnish = input('\033[1;31m\n\n<<<\033[m')

def text_bot():
    os.system("clear")
    print('\033[4;36m<<<BOT WHATSAPP>>>\033[m')

def Print(text,color):
    print('\033[1;{}m{}\033[m'.format(color,text))

def data_information():
    contact = '' # contact catch
    message = '' # message catch

    while contact == "" or contact == "creator>>>": # input of contact
        text_bot()
        Print("\nSe quiser escolher mais de uma pessoa, bote o nome da pessoa que você dejesa enviar mais um virgula. \nEx: Tony,Julia,Thales",32)
        print('\033[1;33m\nPara que você deseja mandar a mensagem?\033[m')

        contact = input('\033[1;31m<<<\033[m') # contact CHOSEN
        if contact == "creator>>>":
            creator()
        else:
            pass

    while message == "": # input of message
        text_bot()
        print("\033[1;33mEscolha a mensagem que voce deseja enviar para \033[1;31m{}\033[m \033[m".format(contact))
        message = input('\033[1;31m<<<\033[m')
    
    contact = contact.split(',')
    the_amount,hours,minutes=perform_shipping_amount()
    return contact,message,the_amount,hours,minutes

def perform_shipping_amount(): 
    global choose_Hours_and_Minutes

    verification = False
    while verification == False:
        text_bot() #show title
        Print('Você deseja enviar mais de uma vez?',33)
        Print('Digite "S" para Sim ou "N" para Não.',32)
        perform_shipping_amount = input('\033[1;32m<<<\033[m') # catch input
        perform_shipping_amount = perform_shipping_amount.upper()

        if perform_shipping_amount == "S" or perform_shipping_amount == "N":
            verification = True
        else:
            text_bot()
            Print("Erro! verifique que você escolheu certo os 'S' ou 'N'!", 31)
            time.sleep(4)
            verification = False

    if perform_shipping_amount == "S":
        text_bot() #show title
        Print("Escolha a quantidade de vezes que o programa deve execultar!", 31)
        the_amount = int(input('\033[1;31m<<<\033[m'))

        if the_amount == 0: # if the_amount is equal the 0 add one
            the_amount = 1

    else:
        the_amount = 1
    
    verification = False

    while verification == False:
        text_bot()
        Print('Voce deseja escolher a hora que o programa pode enviar a mensagem?',33)
        Print('Digite "S" para sim e "N" para não', 32)
        choose_Hours_and_Minutes = input('\033[1;32m<<<\033[m')
        choose_Hours_and_Minutes = choose_Hours_and_Minutes.upper()

        if choose_Hours_and_Minutes == "S" or choose_Hours_and_Minutes == "N":
            verification = True
        else:
            text_bot()
            Print("Erro! verifique que você escolheu certo os 'S' ou 'N'!", 31)
            time.sleep(4)
            verification = False

    if choose_Hours_and_Minutes == "S":
        text_bot()
        Print("Escolha com cuidado a Hora e os minutos!!!",31)
        print("\033[1;33mExemplo de como escolher: {} \033[m".format('\033[4;36m"3:10"\033[m\033[1;33m primeiro vai a horas e depois os minutos.\033[m'))
        time.sleep(2)
        hours_minutes = input('\033[1;31m<<<\033[m')
        hours_minutes = hours_minutes.split(':')
        hours = int(hours_minutes[0])
        minutes = int(hours_minutes[1])

    else:
        hours_minutes = "00:00"
        hours = int(hours_minutes[0])
        minutes = int(hours_minutes[1])

    return the_amount,hours, minutes

def open_browser():
    print('\033[1;33;41mNão feche o Programa !\033[m')
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get('https://web.whatsapp.com/')

    while True:
        text_bot()
        release = input("posso execultar o script? \n Digite 'S' para execultar!\n &:")
        if release.upper() == "S":
            break
        else:
            pass
        
    Print("Espere um pouco...",33)
    return driver

def seek_contact(contact,the_amount,driver):
    i = 0
    while i < len(contact):
        search = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
        time.sleep(3)
        search.click()
        text_bot()
        print('\033[1;30;42m Enviar para: \033[1;31;42m{}\033[m\033[m'.format(contact[i]))
        search.send_keys(contact[i])
        search.send_keys(Keys.ENTER)
        send_message(message,the_amount,driver)
        i = i + 1
    confimation = "message sent!"
    return confimation

def send_message(message,the_amount,driver):
    i = 0
    while i < the_amount:
        message_field = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
        time.sleep(1)
        message_field[1].click()
        print('\033[1;31;44m Mensagem: \033[1;34;40m{}\033[m\033[m'.format(message))
        message_field[1].send_keys(message)
        message_field[1].send_keys(Keys.ENTER)
        i = i + 1

def dateToday():
    Time = time.localtime()
    timehours = Time[3]
    timeminutes = Time[4]
    return timehours,timeminutes
#______________________________________________________bot____________________________________________________________#

text_bot()
contact,message,the_amount,hours,minutes = data_information()
text_bot()
Print("Abrindo o navegador...", 32)
time.sleep(2)
text_bot()

# Two library
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

driver = open_browser()

if choose_Hours_and_Minutes == "S":
    text_bot()
    print('\033[1;33;41mNão feche o Programa !\033[m')
    print("\033[1;31mMensagem vai ser enviada as:\033[1;33m{}\033[m \033[m".format(str(hours)+':'+str(minutes)))

    while True:
        timehours,timeminutes = dateToday()
        if timehours >= hours and timeminutes >= minutes:
            confimation =seek_contact(contact,the_amount,driver) # starting the navigation
            time.sleep(10)
            text_bot()
            print('\033[1;31;46m{}\033[m'.format('Programa Finalizado !'))
            break

else:
    confimation =seek_contact(contact,the_amount,driver) # starting the navigation
    time.sleep(10)
    text_bot()
    print('\033[1;31;46m{}\033[m'.format('Programa Finalizado !'))
