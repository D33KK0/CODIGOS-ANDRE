import os

def limpar_tela():
    print('\n' * 20) 
    os.system('cls')

def adicionar_grupo_familiar(grupo):
    numero_de_filho = int(input('Numero de filhos: '))
    salario = float(input('Digite o salário: '))
    grupo.append({"salario": salario, "numero_de_filhos": numero_de_filho})

def exibir_resultados(grupo):
    if not grupo:
        print('Nunhum dado informado.')
        return

    média_numero_de_filho = sum(p['numero_de_filhos'] for p in grupo=) / len(grupo)
    média_salario = sum(p['salario'] for p in grupo) / len(grupo)

def menu():
    familia = []
    while True:
        print('Menu:')
        print('1 - Adcionar Familia')
        print('2 - Sair e exibir resultados.')
        opc = int(input('Digite a opção no menú: '))
        match opc:
            case 1:
                adicionar_familia(familia)
                limpar_tela()
            case 2:
                exibir_resultados(familia)

