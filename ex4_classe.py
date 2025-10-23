import os
from dataclasses import dataclass
import time

os.system("cls")

# CLASSES
@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: str

# FUNÇÃO PARA MOSTRAR RESULTADOS
    def mostrar_resultados(self):
        print(f'Seu nome: {self.nome}')
        print(f'Seu E-mail: {self.email}')
        print(f'Seu Endereço: {self.endereco}')
    
    def mostrar_nome(self):
        print(f'Nome: {self.nome}')



# TOTAL DE PESSOA
print('==============\033[31mSOLICITANDO DADOS\033[0m==============')
Pessoa1 = Pessoa(nome = input('Digite seu nome: '),
                email = input('Digite seu E-mail: '),
                endereco = input('Digite seu endereço: '))

print('\033[32mPESSOA 1 REGISTRADA!\033[0m')
print('\033[33m...\033[0m')
time.sleep(1.6)
os.system('cls')

print('==============\033[31mSOLICITANDO DADOS\033[0m==============')
Pessoa2 = Pessoa(nome = input('Digite seu nome: '),
                email = input('Digite seu E-mail: '),
                endereco = input('Digite seu endereço: '))

print('\033[32mPESSOA 2 REGISTRADA!\033[0m')
print('\033[33m...\033[0m')
time.sleep(1.6)
os.system('cls')



# MOSTRANDO RESULTADO
print('\033[32mAguardando resultado...\033[0m')
time.sleep(1.5)

print('==============\033[32mDADOS DE EMAIL\033[0m==============')

Pessoa1.mostrar_resultados()
print('\n==========================\n')
Pessoa2.mostrar_resultados()
print('==============\033[32mNOME\033[0m==============')
Pessoa1.mostrar_nome()
Pessoa2.mostrar_nome()
