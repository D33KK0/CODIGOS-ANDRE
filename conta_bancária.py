import os 
os.system('cls')
import time
saldo = 0

# FUNÇÕES PARA BANCO
def tela_do_banco():
	os.system('cls')
	print('..........\033[35mBANCO DO ANDRÉ\033[0m..........')
	print('''SELECIONE:
1 - DEPOSITO
2 - SAQUE
3 - COLSULTAR SALDO''')

# DEPOSITO
def depositar(saldo):
	os.system('cls')
	print('============\033[32mDEPOSITO\033[0m============')
	deposito = float(input('Quanto deseja depositar: '))
	saldo += deposito
	print(f'\033[32mDepósito de R${deposito} reais\033[0m.')
	time.sleep(1.5)
	print('\033[33mVoltando a tela inicial\033[0m...')
	time.sleep(1.3)
	os.system('cls')
	return saldo

# SAQUE
def saque(saldo):
	os.system('cls')
	print('============\033[32mSAQUE\033[0m============')
	valor = float(input('Quanto deseja sacar: '))
	if valor > saldo:
		print('\033[31mSaldo insuficiente para saque\033[0m.')
		print(f'\033[33mSeu saldo é R${saldo} reais\033[0m.')
		valor = float(input('Quanto deseja sacar: '))
		print(f'\033[32mSaque de R${valor} reais\033[0m.')
	else:
		saldo -= valor
		print(f'\033[32mSaque de R${valor} reais\033[0m.')
	time.sleep(1.4)
	print('\033[33mVoltando a tela inicial\033[0m...')
	time.sleep(1.5)
	return saldo

# CONSULTA DE SALDO
def consultar_saldo(saldo):
	os.system('cls')
	print('============\033[32mCONSULTA DE SALDO\033[0m============')
	if saldo < 0:
		print(f'\033[31mSeu saldo é de R${saldo} reais\033[0m')
		print(f'\033[33mVocê está negativado\033[m.')
	
	elif saldo == 0:
		print(f'\033[37mSeu saldo é de R${saldo} reais\033[0m')
		print('\033[33mVocê não possui saldo\033[0m.')
	
	else:
		print(f'\033[32mSeu saldo é de R${saldo} reais\033[0m')

# SOLICITANDO COMANDO
while True:
	tela_do_banco()
	selecionar = int(input('\nSELEÇÃO: '))
	if selecionar ==  1:
		saldo = depositar(saldo)
	elif selecionar ==  2:
		saldo = saque(saldo)
	elif selecionar == 3:
		consultar_saldo(saldo)
		continuar = input('Deseja continuar: ')

		# CASO QUEIRA CONTINUAR OU NÃO
		if continuar.upper().strip() in ['SIM', 'S']:
			os.system('cls')
			tela_do_banco()

		elif continuar.upper().strip() in ['NÃO', 'N']:
			print('FIM')
			time.sleep(1)
			break
	else:
		tela_do_banco()
		print('\033[31mOpção inválida\033[0m.')
		selecionar = int(input('SELEÇÃO: '))


	
		


