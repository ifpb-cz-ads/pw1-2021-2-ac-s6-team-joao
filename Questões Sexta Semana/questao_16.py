numero = int(input('Digite um número: '))

if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print(numero, 'não é primo')
    else:
        print(numero, 'é primo')