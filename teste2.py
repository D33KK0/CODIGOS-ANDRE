mport os
os.system('cls')


def limpar_tela():
    print("\n" * 20)

def adicionar_pessoa(pessoas):
    num_filhos = int(input("Número de filhos: "))
    salario = float(input("Digite o salário: "))
    pessoas.append({"num_filhos": num_filhos, "salario": salario})

def exibir_resultados(pessoas):
    if not pessoas:
        print("Nenhum dado cadastrado.")
        return
    
    media_salario = sum(p['salario'] for p in pessoas) / len(pessoas)
    media_num_filhos = sum(p['num_filhos'] for p in pessoas) / len(pessoas)
    maior_salario = max(p['salario'] for p in pessoas)
    menor_salario = min(p['salario'] for p in pessoas)


    print(f"Média salarial do grupo: R$ {media_salario:.2f}")
    print(f"Média de filhos por familia: {media_num_filhos}")
    print(f"Maior salário do grupo: {maior_salario}")
    print(f"Menor salário do grupo: {menor_salario}")
 

def menu():
    pessoas = []
    while True:
        print("Menu:")
        print("1 - Adicionar familia")
        print("2 - Exibir resultados")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_pessoa(pessoas)
            limpar_tela()
        elif opcao == '2':
            exibir_resultados(pessoas)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()