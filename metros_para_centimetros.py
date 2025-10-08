import os
os.system('cls')

# Logo senai
def logo_senai():
    os.system('cls')
    print('='*7)
    print('SENAI')
    print('='*7)

# Função de conversão 
def conversão_m_para_cm(metros):
    return metros * 100

# Mostrando resultados
altura = float(input('Digite quantos metros você tem: '))
logo_senai()
print(f'Sua altura = {altura:.2f} metros')
print(f'Conversão para centímetros = {conversão_m_para_cm(altura):.1f} cm')
