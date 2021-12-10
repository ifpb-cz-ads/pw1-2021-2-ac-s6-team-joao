divida = int(input('Digite a divida a ser paga: '))
pagar = 0
pagMes = 0
dividaJuros = 0
mes = 0

while divida > 0:
    pagar = int(input('Digite quanto você irá pagar: '))
    divida = divida - pagar
    print('Foram pagos R$', pagar, 'esse mês. Restam R$', divida)
    
    if divida > 0:
        dividaJuros = int(input('Digite os juros da divida: '))
        divida = divida + (divida * (dividaJuros/100))
        print('Com os juros de', dividaJuros,'por cento. A divida subiu para R$', divida)
        
    mes = mes + 1
    
print(mes,'meses para pagar.')