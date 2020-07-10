# Programa que busca números maiores que 50.
#
#
# Secao 9 exercicio 05
#
#
# Entrada
n = 0
lista = []
lista50 = []

# Processamento\ Saída
for i in range(1, 11):
    n = int(input(f"Informe um número {i}/10: "))
    lista.append(n)
    if n > 50:
        lista50.append(n)
        
print(lista)

for i in range(0,10):
    if lista[i] > 50:
        print(f"O número {lista[i]} está na posição {i}.")    
    
if len(lista50) == 0:
    print('Não existe números maiores que 50 na lista')   



