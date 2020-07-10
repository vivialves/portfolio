# Tabuada ( Multiplication table )

# Secao 8 exercicio 6

print("Vamos contar tabuada ... De 1 até 10!")

# Entrada
t = 0

# Processamento
n = int(input("Informe um número entre 1 e 10: "))

while n < 0 or n > 10:
    print("Informe qualquer número inteiro entre 1 e 10...")
    n = int(input("Informe um número: "))

print(f"Tabuada de {n}")

while t != 10:
    t = t + 1
    print(f"{n} x {t} = {t * n}")
    