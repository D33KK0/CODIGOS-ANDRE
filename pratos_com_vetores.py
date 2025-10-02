import os
os.system('cls')

list_preço = []
list_pratos = []

# ANUNCIADO
while True:
    código = int(input('''
Código =========== Pratos =========== Valor
1                  PICANHA            R$25,00
2                  LASANHA            R$20,00
3                  STROGONOFF         R$18,00
4                  BIFE ACEBOLADO     R$15,00
5                  PÃO COM OVO        R$5,00

Digite o código do pedido: '''))

# CRITERIO DE ESCOLHA
    match código:
        case 1:
            prato = 'PICANHA'
            preço = 25
            print('\n\033[35mPICANHA\033[0m SELECIONADO.\n\033[32mR$25,00\033[0m reais') 
        case 2:
            prato = 'LASANHA'
            preço = 20
            print('\n\033[34mLASANHA\033[0m SELECIONADO.\n\033[32mR$20,00\033[0m reais')  
        case 3:
            prato = 'STROGONOFF'
            preço = 18
            print('\n\033[33mSTROGONOFF\033[0m SELECIONADO.\n\033[32mR$18,00\033[0m reais')
        case 4:
            prato = 'BIFE ACEBOLADO'
            preço = 15
            print('\n\033[32mBIFE ACEBOLADO\033[0m SELECIONADO.\n\033[32mR$15,00\033[0m reais') 
        case 5:
            prato = 'PÃO COM OVO'
            preço = 5
            print('\n\033[31mPÃO COM OVO\033[0m SELECIONADO.\n\033[32mR$5,00\033[0m reais')
        case _:
            print('\033[36mNEHUM PRATO ESCOLHIDO.\033[0m')
    if código >= 1 and código <= 5:
        list_pratos.append(prato)
        list_preço.append(preço)

# ESCOLHER OUTRO PRATO
    continuar = str(input('Deseja escolher outro prato: (SIM/NÃO): ')).upper().strip()
    if continuar == ['NÃO', 'NAO', 'N']:
        break
    os.system('cls')

# MOSTRANDO RESULTADOS
if sum(list_preço) == 0:
    print('\033[31mNENHUM PRATO ESCOLHIDO.\033[0m')
else:
    print('\033[32mPRATOS ESCOLHIDOS\033[0m')
    for prato in list_pratos:
        print(f'Pratos escolhidos: {prato}')

    print(f'Preço total: R$\033[32m{sum(list_preço)}\033[0m reais ')
print('FIM')
        


