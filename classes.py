import os
os.system('cls')

from dataclasses import dataclass

@dataclass
class pessoa:
    nome: str
    idade: int
    cpf = str

@dataclass
class pet:
    nome: str
    idade: int
    peso: float

# exemplo de uso de classe
pessoa1 = pessoa(nome ='Alice', idade = 30, cpf = '89234564654' )
pet1 = pet(nome='Marlon', idade=15, peso=25.6)

print