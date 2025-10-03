import os
os.system('cls')

# Função negativos
def positivo_negativo(numero):
    if numero > 0:
        print('\033[32mPOSITIVO\033[0m.')
    elif numero < 0:
        print('\033[31mNEGATIVO\033[0m')
    else:
        print('\033[33mNEUTRO\033[0m')

# Digitar numero para saber se é positivo ou negativo
numero = int(input('Digite um número: '))
positivo_negativo(numero)
