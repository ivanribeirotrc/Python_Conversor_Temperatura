# Autor: Ivan Ribeiro
# Descrição: Simples conversor de temperatura (Celsius para Fahrenheit e vice-versa)
# Data: 22/12/2021

import time
import colorama
from colorama import Fore


def main():
    print('Temperaturas: ' + Fore.YELLOW + 'Celsius' + Fore.RESET + ' | ' + Fore.YELLOW + 'Fahrenheit' + Fore.RESET)
    conv = input('Digite a inicial da temperatura que será convertida: ')
    if conv == 'c':
        t1 = float(input('Informe o valor da temperatura em Celsius que será convertida: '))
        t2 = float(t1 * 9/5) + 32
        print('A Conversão de %2.f' % t1 + ' Graus ' + Fore.YELLOW + 'Celsius' + Fore.RESET + ' para Fahrenheit foi de: %2.f' % t2 + ' Graus ' + Fore.YELLOW + 'Fahrenheit' + Fore.RESET)
        time.sleep(1)
        menu = input('Digite [S] para realizar outra conversão ou insira qualquer letra para sair do programa: ')
        if menu == 's':
            main()
        else:
            print('Obrigado por utilizar nosso programa, até breve!')
            time.sleep(2)
            return
    elif conv == 'f':
        t1 = float(input('Informe o valor da temperatura em Fahrenheit que será convertida: '))
        t2 = float(t1 - 32) * 5/9
        print('A Conversão de %.2f' % t1 + ' Graus ' + Fore.YELLOW + 'Fahrenheit' + Fore.RESET + ' para Celsius foi de: %.2f' % t2 + ' Graus ' + Fore.YELLOW + 'Celsius' + Fore.RESET)
        time.sleep(1)
        menu = input('Digite [S] para realizar outra conversão ou insira qualquer letra para sair do programa: ')
        if menu == 's':
            main()
        else:
            print('Obrigado por utilizar nosso programa, até breve!')
            return
    else:
        print('Favor selecione uma temperatura VALIDA')
        main()


colorama.init()
print('Conversor de temperaturas by ' + Fore.RED + 'Ivan Ribeiro' + Fore.RESET)
time.sleep(1)
main()
