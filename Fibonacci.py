# Função que escreve a sequencia de Fibonacci, o usuário escolhe o numero.
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

# Saída
n = int(input('Informe um número: '))
fib(n)