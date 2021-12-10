numero = int(input('Digite o número: '))
x = 1
operacao = 0

print('1 - adicão;')
print('2 - subtração;')
print('3 - multiplicação;')
print('4 - divisão;')
print('5 - saída;')

menu = int(input())

if menu == 1:
    while x <= 10:
        
        operacao = numero + x
        print(numero,'+', x,'=', operacao)
        x = x + 1

if menu == 2:
    while x <= 10:
        operacao = x - numero
        print(x,'-', numero,'=', operacao)
        x = x + 1

if menu == 3:
    while x <= 10:
        
        operacao = numero * x
        print(numero,'x', x,'=', operacao)
        x = x + 1
        
if menu == 4:
    while x <= 10:
        operacao = x / numero
        print(x,'/', numero,'=', operacao)
        x = x + 1
        
if menu == 5:
    print('Saiu.')