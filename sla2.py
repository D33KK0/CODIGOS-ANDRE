
import os
os.system("cls")

quantidade_numeros = 0
soma = 0
numeros_par = 0
numero_impar = 0
pares = 0
impares = 0

    # EXECUÇÃO DOS CODIGOS

while True:
    nota = int(input('Digite um número: '))
    if nota > 0: 
        quantidade_numeros += 1
        soma += nota
        if nota % 2 == 0:
            pares += 1
            numeros_par += nota
        else:
            impares += 1
            numero_impar += nota
    if nota == 0:
        break

    #CALCULANDO

média_par = numeros_par / pares
média_impares = numero_impar / impares

    #EXIBINDO VALORES

print(f'Soma dos valores digitados {soma}')
print(f'Quantidade de impares {impares}')
print(f'Quantidade de pares {pares}')
print(f'Média par {média_par:.2f}')
print(f'Média impares {média_impares:.2f}')
