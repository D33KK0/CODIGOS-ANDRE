import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Aluno:
    nome: str
    idade: int
    email: str
    telefone: int

def tela_inicial():
    print('=================\033[34mINSCRIÇÃO SENAI\033[0m=================')
    print('\n\033[33mSolicitando dados do aluno.\033[0m')

QUANTIDADE_ALUNOS = 2
listra_alunos = []

for i in range(QUANTIDADE_ALUNOS):
    tela_inicial()
    aluno = Aluno(nome= input('Nome: '),
                  idade= int(input('Idade: ')),
                  email= input('E-mail: '),
                  telefone= int(input('Telefone: ')))
    os.system('cls')
    
    listra_alunos.append(aluno)

arquivo = 'dados_aluno.txt'

with open(arquivo, 'a') as arquivo_aluno:
    for aluno in listra_alunos:
        arquivo_aluno.write(f'{aluno.nome}, {aluno.idade}, {aluno.email}, {aluno.telefone}\n')
    print('\033[32mSalvo com sucesso!\033[0m')