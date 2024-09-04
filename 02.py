def fibonacci(numero):
    a=0
    b=1
    while b < numero:
        a, b = b, a + b
    return b == numero or numero == 0

numero = int(input("Informe um número: "))
if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
