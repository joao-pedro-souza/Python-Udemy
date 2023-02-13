"""
Iterando strings com while
"""

#       012345678910
nome = 'Luiz Otávio'
#     -1110987654321
tamanho_nome = len(nome)
contador = 0
nova_string = ''

while contador < tamanho_nome:
    letra = f'*{nome[contador]}'
    nova_string += letra
    contador += 1

print(nova_string)