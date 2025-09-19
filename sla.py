import os
os.system('cls')

    #CARDÁPIO

valor_total = 0
preço = 0

print('''
Código      Prato           $
      
1    --->   PICANHA       R$25,00
2    --->   LASANHA        R$20,00
3    --->   STROGONOFF    R$18,00
4    --->   BIFE AC       R$15,00
5    --->   PÃO c/ OVO    R$5,00  ''')  
print('\n=====================================')
    
    #ESCOLHER CARDÁPIO  

código = str(input('\nQual Código do pedido: '))

    #RESULTADO DO PEDIDO

match código:
    case 1:
        preço = 25
        print('\nCOMFIRMADO *PICANHA*!\nPREÇO = R$25,00')
    case 2:
        preço = 20
        print('\nCOMFIRMADO *LASANHA*!\nPREÇO = R$20,00')
    case 3:
        preço = 18
        print('\nCOMFIRMADO *STROGONOFF*!\nPREÇO = R$18,00')
    case 4:
        preço = 15
        print('\nCOMFIRMADO *BIFE ACEBOLADO*!\nPREÇO = R$15,00')
    case 5:
        preço = 5
        print('\nCOMFIRMADO *PÃO C/ OVO*!\nPREÇO = R$5,00')
    
    #OPÇÃO DE ESCOLHER DE NOVO

opção_de_segunda_compra = input('\nDeseja fazer mais um pedido?(s/n): ').upper()

    #CASO A OPÇÃO NAO SEJA N E S

while opção_de_segunda_compra not in 'S' 'N':
    opção_de_segunda_compra = input('\nERRO. Deseja fazer mais um pedido?(s/n): ').upper()

    #CONDIÇÃO DE PRATO DO SEGUNDO PEDIDO...

if opção_de_segunda_compra == 'S':

    #REPETIÇÃO CASO QUEIRA COMPRAR VAIROS PRATOS

    while opção_de_segunda_compra == 'S':
        código2 = input('\nQual Código do pedido: ')

    #RESULTADO DO PEDIDO

        match código:
            case 1:
                preço = 25
                print('COMFIRMADO *PICANHA*!\nPREÇO = R$25,00')
            case 2:
                preço = 20
                print('COMFIRMADO *LASANHA*!\nPREÇO = R$20,00')
            case 3:
                preço = 18
                print('COMFIRMADO *STROGONOFF*!\nPREÇO = R$18,00')
            case 4:
                preço = 15
                print('COMFIRMADO *BIFE ACEBOLADO*!\nPREÇO = R$15,00')
            case 5:
                preço = 5
                print('COMFIRMADO *PÃO C/ OVO*!\nPREÇO = R$5,00')
        opção_de_segunda_compra = input('\nDeseja fazer mais um pedido?(s/n): ').upper()
        
        #CASO OPÇÃO ESTEJA FORA DE S OU N

        while opção_de_segunda_compra not in 'S' 'N':
            opção_de_segunda_compra = input('\nERRO. Deseja fazer mais um pedido?(s/n): ').upper()
        
        #CASO NAO QUEIRA MAIS COMPRAR
        
        if opção_de_segunda_compra == 'N':
            valor_total = valor_total + preço
            print(f'VALOR TOTAL = {valor_total}')
    

    
    