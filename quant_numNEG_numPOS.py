import os
os.system('cls')

# Variáveis
NUMEROS_ADICIONADORS = 5
numeros_negativos = 0
numeros_positivos = 0
total_de_numeros = []

# Adicionar numeros
for i in range(NUMEROS_ADICIONADORS):
    numeros = int(input(f'Digite \033[36m{i+1}\033[0m N°: '))
    total_de_numeros.append(numeros)
    if numeros < 0:
        numeros_negativos += 1
    else:
        numeros_positivos += numeros
print(f'Quandidade de numeros \033[31mNegativos\033[0m = \033[37m{numeros_negativos}\033[0m')
print(f'Soma de numeros \033[32mPositivos\033[0m = \033[37m{numeros_positivos}\033[0m')
