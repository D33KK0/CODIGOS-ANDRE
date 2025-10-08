import os
os.system('cls')

# Logo do senai
def logo_senai():
    os.system('cls')
    print('='*7)
    print('SENAI')
    print('='*7)

# Função divisão
def subtração(numero1, numero2):
    return numero1 - numero2

# Função Multiplicação
def multiplicação(numero1, numero2):
    return numero1 * numero2

# Função Divisão
def divisão(numero1, numero2):
    return numero1 / numero2 if numero2 != 0 else '\033[33mDivisão por 0\033[0m'

# Função Soma
def soma(numero1, numero2):
    return numero1 + numero2

# Mostrar resultado
logo_senai()

numero1 = int(input('Digite o \033[36m1\033[0mº numero: '))

logo_senai()
numero2 = int(input('Digite o \033[36m2\033[0mº numero: '))

logo_senai()
print(f'Números = {numero1}, {numero2}')
print(f'\n\033[31mSubtração\033[0m = {subtração(numero1, numero2)}')
print(f'\033[32mAdição\033[0m = {soma(numero1, numero2)}')
print(f'\033[35mMultiplicação\033[0m = {multiplicação(numero1, numero2)}')
print(f'\033[34mDivisão\033[0m = {divisão(numero1, numero2)}')

# Opção de continuar
continuar = input('Quer continuar: ')
logo_senai()
     