import os
os.system('cls')

# VALOR DOS PRATOS
valor_picanha = 25
valor_lasanha = 20
valor_strogonoff = 18
valor_bife_acebolado = 15
valor_pão_com_ovo = 5

# ANUNCIADO
print ('''
Código =========== Pratos =========== Valor
1                  PICANHA            R$25,00
2                  LASANHA            R$20,00
3                  STROGONOFF         R$18,00
4                  BIFE ACEBOLADO     R$15,00
5                  PÃO COM OVO        R$5,00
        ''')

# ESCOLHA DOS PRATOS
while True:
    código = int(input('Digite o código do pedido: '))
    if código > 5:
        print('erro')      
    match código:
        case 1:
            valor_picanha = 25
            valor_picanha += 
            print('\n\033[35mPICANHA\033[0m SELECIONADO.\n\033[32mR$25,00\033[0m reais')
            
        case 2:
            valor_lasanha = 20
            print('\n\033[34mLASANHA\033[0m SELECIONADO.\n\033[32mR$20,00\033[0m reais')
            
        case 3:
            valor_strogonoff = 18
            print('\n\033[33mSTROGONOFF\033[0m SELECIONADO.\n\033[32mR$18,00\033[0m reais')
        
        case 4:
            valor_bife_acebolado = 15
            print('\n\033[32mBIFE ACEBOLADO\033[0m SELECIONADO.\n\033[32mR$15,00\033[0m reais')
            
        case 5:
            valor_pão_com_ovo = 5
            print('\n\033[31mPÃO COM OVO\033[0m SELECIONADO.\n\033[32mR$5,00\033[0m reais')
    outr_prato = input('\n\033[33mDeseja escolher outro prato\033[0m: ')
    if outr_prato == 'NÃO' 'NAO' 'N':

        break
        


