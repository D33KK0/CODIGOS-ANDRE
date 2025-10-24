from dataclasses import dataclass
import os
os.system('cls')
import time

# CLASSES
@dataclass
class dados:
    nome: str
    idade: int
    peso: float
    altura: float

    def dados_pessoais(self):
        print(f'\033[33mNome\033[0m: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Peso: {self.peso}')
        print(f'Altura: {self.altura}')

# SOLICITANDO DADOS PESSOAIS
lista_de_pessoas = []
for i in range(3):
    print(f'=================\033[36mSOLICITANDO DADOS PESSOAIS {i+1}\033[0m=================')
    pessoa = dados(nome= input('Digite seu nome: '),
                   idade= int(input('Digite sua idade: ')),
                   peso= float(input('Digite seu peso: ')),
                   altura= float(input('Digite sua altura: ')))
    print('\033[32mCADASTRADO!\033[0m')
    lista_de_pessoas.append(pessoa)
    time.sleep(1)
    os.system('cls')

# RESULTADO
for ordem, pessoa in enumerate (lista_de_pessoas, start=1):
    print(f'{ordem}º PESSOA')
    pessoa.dados_pessoais()
    print('--------------------------\n')