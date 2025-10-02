import os
os.system("cls")
import colorama

# Criando um vetor (lista).
lista_numeros = []
quantidade_de_números = 6
quant_pares = 0
quant_impares = 0
num_pares = []
num_impares = []

# Anunciado
print('\033[32mPARES\033[0m E \033[31mIMPARES\033[0m\n')

# Inserindo notas
for i in range(quantidade_de_números):
    numeros = int(input(f"Digite a \033[3m{i+1}\033[0mª N°: "))
    lista_numeros.append(numeros)

    # Contagem dos impares e pares
    if numeros % 2 == 0:
        quant_pares += 1
        num_pares.append(numeros)
    else:
        quant_impares += 1
        num_impares.append(numeros)

# Mostrando resultados
print(f'\nExistem \033[30m{quant_pares}\033[0m n° \033[32mpares\033[0m')
print(f'São eles {num_pares}')
print(f'\nExistem \033[30m{quant_impares}\033[0m n° \033[31mimpares\033[0m')
print(f'São eles {num_impares}')