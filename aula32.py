"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

str_numero = input('Digite um número inteiro: ')
int_numero = None

try:
    int_numero = int(str_numero)
except:
    print('Você não digitou um numero inteiro')

if int_numero is not None:
    if int_numero % 2 == 0:
        print(f'{int_numero} é par')
    else:
        print(f'{int_numero} é ímpar')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""