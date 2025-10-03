import os
os.system('cls')

# Caracteristicas
def saudação(nome, altura, peso, idade):
    os.system('cls')
    print(f'Olá, \033[34m{nome}\033[0m! Seja bem vindo!')
    print(f'Sua altura é {altura}cm.')
    print(f'Seu peso é {peso}kg.')
    print(f'Sua idade é {idade} anos.')

# Informar caracteristica
nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
idade = int(input('Digite sua idade: '))
saudação(nome, altura, peso, idade)
