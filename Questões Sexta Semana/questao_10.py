deposito = int(input('Digite quanto você irá depositar: '))
juros = int(input('Digite a porcentagem de juros: '))
meses = 1
ganhoJuros = deposito + (deposito * (juros/100))
x = 0

while meses <= 12:
    x = x + ganhoJuros
    print(x)
    
    meses = meses + 1