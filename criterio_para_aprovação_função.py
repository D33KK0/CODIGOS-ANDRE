import os
os.system('cls')
total_de_notas = 2
lista_notas = []

# Função média/Criério de aprovação
def média(nota):
    if média < 7:
        print('\033[31mREPROVADO\033[0m')
    else:
        print('\033[32mAPROVADOS\033[0m')
    return sum(lista_notas) / total_de_notas
    
    
# Solicitando notas
for i in range(total_de_notas):
    nota = float(input(f'Digite {i+1}º nota: '))
    lista_notas.append(nota)

# Mostrando resultados
print(f'Suas notas = \033[33m{lista_notas}\033[0m')
print(f'Sua média = \033[33m{média(nota):.2f}\033[0m')