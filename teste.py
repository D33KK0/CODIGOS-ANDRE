from dataclasses import dataclass
import os
import time

os.system('cls')

@dataclass
class Endereco:
    lagradouro: str
    numero = int

    def dados_de_entrega(self):
        print(f'Lagradouro: {self.lragradouro}')
        print(f'Número: {self.numero}')

@dataclass 
class Pessoa:
    nome: str
    idade: int
    Endereco: Endereco

    def dados_pessois(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Endereco: {self.Endereco}')

# SOLICINDO DADOS
endereço1 = Endereco(lagradouro= input('Digite seu lagradouro: '))
        
pessoa1 = Pessoa(nome= input('Digite seu nome: '),
                 idade= int(input('Digite sua idade: ')),
                 Endereco= Endereco) 
