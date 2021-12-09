deposito = 0
juros = int(input('Digite a porcentagem de juros: '))
meses = 1
ganhoJuros = 0
x = 0

while meses <= 12:
    deposito = int(input('Digite quanto você irá depositar: '))
    ganhoJuros = deposito + (deposito * (juros/100))
    x = x + ganhoJuros
    print(x)
    
    meses = meses + 1