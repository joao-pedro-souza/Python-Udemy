"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
contador = 0

for nome in lista:
    print(f'{contador} {nome}')
    contador += 1