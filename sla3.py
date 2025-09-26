import os 
os.system('cls')
import time

    #LIMPA A TELA POR 20 LINHAS

def limpar_tela():
    print('\n' * 20)

    # DEFINIR "ADCINAR NOVA PESSOA" PARA PESQUISA

def adicionar_pessoa (grupo):
    idade = int(input('Digite a idade'))
    sexo = str(input('Digite o sexo (M/F): ')).upper()
    salario = float(input('Digite o salário: '))
    grupo.append({"idade": idade, "sexo": sexo, "salario": salario})

    #
    

def exibir_resultado (grupo):
    if not grupo:
        print('Nenhum dado cadastrado.')
        return
    
média_salario = sum(p['salario'] for p in grupo) / len(grupo)

def menu():
    grupo = []
    while True:
        print('Menu:')
        print('1 - Adcionar pessoa')
        print('2 - Exibir resultado')
        print('3 - Sair')
        opc = int(input('Digite a opção: '))
        match opc:
            case 1:
                adicionar_pessoa(grupo)
                limpar_tela() 
            case 2:
                exibir_resultado(grupo)
            case 3:
                print('Saindo...') 
                time.sleep(1)
                break
            case _:
                print('Opção inválida! Tente novamente.')

if __name__ == '__main__':
    menu()