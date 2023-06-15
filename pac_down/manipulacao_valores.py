#Dois valores somar,multiplicar,qual o maior,novos valores,sair 
from time import sleep
print('====MANIPULAÇÃO DE VALORES NUMERICOS====')
print('=+' *20)
op = int(6)
num1 = int(input('Escolha o primeiro numero :'))
num2 = int(input('Escolha o segundo numero :')) 
sleep(2)   
print('=+' *20)
while op == 6 : 
    print('===Escolha o que acontece===')
    print('[1]Somar os valores \n[2]Multiplicar os valores \n[3]Ver qual valor e maior \n[4]Usar novos valores \n[5]Finalizar')
    print('=+' *20)
    op = int(input('escolha :'))
    if op == 1 :
        print ('o Resultado e :{}'.format(num1 + num2))
        sleep(3)
        op = 6
    if op == 2 :
        print ('o Resultado e :{}'.format(num1 * num2))
        sleep(3)
        op = 6
    if op == 3 :
        if num1 > num2 :
            print ('o Resultado e :{}'.format(num1))
        elif num2 > num1 :
            print ('o Resultado e :{}'.format(num2))
        else :
            print ('Os Valors são os mesmos')
        sleep(3)
        op = 6
    if op == 4 :
        num1 = int(input('Escolha o primeiro numero :'))
        num2 = int(input('Escolha o segundo numero :'))
        sleep(2)
        op = 6
print('Programa Finalizado !!!')
