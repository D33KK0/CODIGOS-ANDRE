import os
os.system('cls')

tota_de_nota = 0
soma = 0

while True:

    nota = float(input('Nota: '))
    nota = float(input('Nota: '))

    tota_de_nota += 1
    soma += nota
    opc_adicionar_mais_nota = input('Quer adicionar mais notas?(s/n): ').upper()
    
    if opc_adicionar_mais_nota == 'N':
        break

média =  soma / tota_de_nota
print(f'Média = {média:.2f}')
