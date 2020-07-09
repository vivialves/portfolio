# Escreva um algoritmo que leia certa quantidade de números e imprimima o maior deles e quantas vezes o maior número foi lido.

n18 = 0
lista_c = []

print('Give me the quantity of numbers for read: ')
qtd = int(input())

while len(lista_c) != qtd:
    print('Give me the numbers of the list: ')
    n18 = int(input())
    if len(lista_c) != qtd:
        lista_c.append(n18)

print(max(lista_c))
print(lista_c.count(max(lista_c)))