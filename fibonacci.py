def fibonacci(num):
    if num == 0:
        return 1
    elif num == 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


num = int(input("Digite um número: "))

if num < 0:
    print("Número inválido")

i = 0
print("Sequência de Fibonacci: ")

for i in range(0, num):
    print(fibonacci(i))
