from dataclasses import dataclass
import os
os.system('cls')
import time

# CLASSES
@dataclass
class Cliente:
    endereco: str
    lagradouro: str
    numero: int
    cidade: str
    nome: str
    email: str

    
    # MOSTRAR DADOS DE ENTREGA
    def mostrar_dados_de_entrega(self):
        print('============\033[32mDADOS DE ENTREGA\033[0m============')
        print(f'Endereço: {self.endereco}')
        print(f'Lagradouro: {self.lagradouro}')
        print(f'N°: {self.numero}')
        print(f'Cidade onde reside: {self.cidade}')


    # MOSTRAR DADOS PESSOAIS
    def mostrar_dados_pessoais(self):
        print('============\033[32mDADOS PESSOAIS\033[0m============')
        print(f'Seu nome: {self.nome}')
        print(f'Seu E-mail: {self.email}')

# SOLICITANDO INFORMAÇÕES DE ENTREGA E DADOS PESSOAIS
print(f'================\033[33mSOLICITANDO DADOS PESSOAIS\033[0m================')
cliente1 = Cliente(nome = input('Nome: '), 
                    email = input('E-mail: '),
                    endereco= input('Endereço: '), 
                                   lagradouro= input('Lagradouro: '), 
                                   numero= int(input('N°: ')), 
                                   cidade= input('Cidade onde reside: '))

# PAUSA 
print('------------------------------\n\033[32mCADASTRADO!\033[0m')
time.sleep(1.5)
os.system('cls')

print('\033[32mCARREGANDO...\033[0m')
time.sleep(1.2)
os.system('cls')


# RESULTADO FINAL

cliente1.mostrar_dados_de_entrega()
time.sleep(0.5)
cliente1.mostrar_dados_pessoais()