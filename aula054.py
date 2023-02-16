"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    escolha_usuario = input('[i]nserir [a]pagar [l]istar: ')
    
    if escolha_usuario.lower() == 'i':
        os.system('cls')
        item_lista = input('Valor: ')
        lista.append(item_lista)

    elif escolha_usuario.lower() == 'a':
        os.system('cls')
        valor = input('Valor: ')
        try:
            indice = int(valor)
            lista.pop(indice)
        except:
            print('Esse valor não existe')

    elif escolha_usuario.lower() == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Lista vazia')
        else:
            for índice, nome in enumerate(lista):
                print(índice, nome) 
    else:
        print('Por favor digite i, a ou l')