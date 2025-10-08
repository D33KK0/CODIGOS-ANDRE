import os 
os.system('cls')

# Logo do senai
def logo_senai():
    os.system('cls')
    print('='*7)
    print('SENAI')
    print('='*7)

# Função de definir a inflação
def inflação(preço):
    if preço <= 100:
        print(f'O preço de R${preço} reais, com inflação de 10% ficará \033[33mR${preço + ((10/100) * preço):.2f} reais\033[0m')
    else:
        print(f'O preço de R${preço} reais, com inflação de 20% ficará \033[33mR${preço + ((20/100) * preço):.2f} reais\033[0m')

# Mostrando resultados
print('Preços < 100 = 10% de inflação\nPreço > 100 = 20% de inflação\n')
preço = float(input('Digite o preço de um produto: '))
inflação(preço)