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

# FUNCÕES
    def dados_entrega(self):
        print('DADOS DE ENTREGA')
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")

    def dados_email_marketing(self):
        print('DADOS DE E-MAIL')
        print(f'Nome: {self.nome}')
        print(f'E-mail: {self.email}')

# INFORMAÇÕES
print('============\033[33mSOLICITANDO INFORMAÇÕES\033[0m============')
Pessoa1 = Pessoa(nome = input('Digite seu nome: '),
                email = input('Digite seu E-mail: '),
                endereco = input('Digite seu endereço: '))

print('===========\033[32mEXIBINDO DADOS DE ENTREGA\033[0m===========')
Pessoa1.dados_email_marketing()
print('\033[34mCarregando...\033[0m')
time.sleep(1.6)
print('===========\033[32mEXIBINDO DADOS DE E-MAIL\033[0m===========')
Pessoa1.dados_entrega()

