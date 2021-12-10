numero = 0
n = int(input('Digite a quantidade: '))
x = 0

while x <= n:

    numero = int(input('Digite um número: '))

    if numero > 1:
        for i in range(2, numero):
            if numero % i == 0:
                print(numero, 'não é primo')
        else:
            print(numero, 'é primo')
    x = x + 1