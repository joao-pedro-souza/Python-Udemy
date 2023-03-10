"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""
cpf_usuario = '74682489070'
nove_digitos = cpf_usuario[:9]
soma_digitos = 0

n = 10
for digito in nove_digitos:
    soma_digitos += int(digito) * n
    n -= 1

soma_vezes_10 = soma_digitos * 10
resto_divisao = soma_vezes_10 % 11

if resto_divisao > 9:
    primeiro_digito = 0
else:
    primeiro_digito = resto_divisao

dez_digitos = nove_digitos + str(primeiro_digito)
print(dez_digitos)

soma_digitos = 0
n = 11
for digito in dez_digitos:
    soma_digitos += int(digito) * n
    n -= 1

soma_vezes_10 = soma_digitos * 10
resto_divisao = soma_vezes_10 % 11

if resto_divisao > 9:
    segundo_digito = 0
else:
    segundo_digito = resto_divisao

cpf_gerado = cpf_usuario[:9] + str(primeiro_digito) + str(segundo_digito)

if cpf_usuario == cpf_gerado:
    print('CPF Válido!')
else:
    print('CPF Inválido')
