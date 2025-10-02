import os
os.system("cls")
import colorama

# Criando um vetor (lista).

lista_notas = []
QUANTIDADE_DE_NOTAS = 3

# Inserindo notas

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)

    # SOMA E MÉDIA DAS NOTAS
    soma = sum(lista_notas)
    média = soma / QUANTIDADE_DE_NOTAS

    # MAIOR E MENOR NOTA
    menor = min(lista_notas)
    maior = max(lista_notas)

# FINAL DO CÓDIGO

print(f'\nNotas informadas {lista_notas}')
print(f'\nMaior_nota = {maior}')
print(f'\Menor_nota = {menor}')

if média >= 7:
    print(f'\nMédia = {média:.2f}.\n\033[32mAPROVADO!\033[0m')
elif média >= 5 and média < 7:
    print(f'\nMédia = {média:.2f}.\n\033[33mRecuperação!\033[0m')
elif média <= 5:
    print(f'\nMédia = {média:.2f}.\n\033[31mREPROVADO!\033[0m')