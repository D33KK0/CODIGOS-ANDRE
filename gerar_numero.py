import random
import os
os.system('cls')

numeros = [1, 2, 3,]
escolha_maquina = random.choice(numeros)

escolha = int(input('Escolha um número de 1 a 3: '))
if escolha == escolha_maquina:
	print('\033[32mVocê acertou\033[m!')
else:
	print('\033[31mVocê errou\033[0m.')
	print(f'Máquina: Meu número é {escolha_maquina}.')