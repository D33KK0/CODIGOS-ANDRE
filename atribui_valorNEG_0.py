import os
os.system('cls')

# Variáveis
lista_de_numeros = []
# TOTAL_DE_NUMEROS = 5
numeros_pos = 0
numeros_neg = 0
lista_pos = []
lista_neg = []

# Escolher quantos numeros adicionar para contagem
escolha = int(input('\033[36mQuantos números quer adicionar para contagem\033[0m: '))

# Caso escolha seja <= 0
if escolha <= 0:
    print(f'\033[31mVocê não digitou nenhum número.\033[0m')

# Adicionar números
for i in range(escolha):
    numeros = int(input('Digite um número: '))
    lista_de_numeros.append(numeros)

# Condições para números
    if numeros <= 0:
        numeros = 0
        lista_neg.append(numeros)
        numeros_neg += 1
    else:
        numeros_pos += 1
        lista_pos.append(numeros)

# Mostrando resultados
print(f'\nVocê digitou {numeros_pos} N° \033[32mPOSITIVOS\033[0m.\nSão eles \033[33m{lista_pos}\033[0m')
print(f'\nVocê digitou {numeros_neg} N° \033[31mNEGATIVO(s)\033[0m que virou(ram) \033[34mNEUTRO\033[0m.\nSão eles \033[33m{lista_neg}\033[0m\n')

for numes in (lista_de_numeros):
    print(f'Todos os números adicionados: \033[33m{numeros}\033[0m')
    print('=' * 10)