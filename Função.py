import os
os.system('cls')

# Função tabuada
def calculadores(numero):
    for i in range(10+1):
        print(f'\033[33m{numero}\033[0m x \033[33m{i}\033[0m = \033[32m{numero * i}\033[0m')

# Numero para calcular tabuada
numero = int(input('Digite um número para vermos a sua tabuada: '))
calculadores(numero)