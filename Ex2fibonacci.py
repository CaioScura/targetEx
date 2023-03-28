def fibonacci(num):
    if (num <= 1):
        return num
    else:
        #calculo de fibonacci
        return fibonacci(num-2) + fibonacci(num - 1)

print("Informe um numero: ")
num = int(input())

i = 0

while fibonacci(i) < num:
    i+=1

#verificar se o numero esta presente na sequencia
if fibonacci(i) == num:
    print(num," pertence a sequencia de Fibonacci")
else:
    print(num," NÃO pertence a sequencia de Fibonacci")
