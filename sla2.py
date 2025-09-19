
import os
os.system("cls")

quantidade_numeros = 0
soma = 0
numeros_par = 0
numero_impar = 0
numeros = 0

while True:

    soma += numeros    
    quantidade_numeros += 1
    numeros += int(input('Digite um valor: '))

    if numeros % 2 == 0:
        numeros_par += numeros
        média_par = soma / numeros_par 

    elif numeros % 3 == 0:
        numeros_impar += 1
        média_impar = soma / numeros_impar
    
        if numeros < 0:
            break

média_geral = soma / quantidade_numeros    
qnt_numeros_pares_e_impares = numeros_impar + numeros_par

print(f'Quantidade de números pares e impares = {qnt_numeros_pares_e_impares}')
print(f'Média dos valores pares = {média_par}')
print(f'Média geral = {média_geral}')