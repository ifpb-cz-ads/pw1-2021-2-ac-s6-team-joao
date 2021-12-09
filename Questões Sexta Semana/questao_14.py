codigo = 1
preco = 0
quantidade = 0
soma = 0

while codigo != 0:
    
    codigo = int(input('Digite o código do produto: '))
    
    if codigo == 1:
        quantidade = int(input('Digite a quantidade: '))
        soma = quantidade * 0.50
        
    if codigo == 2:
        quantidade = int(input('Digite a quantidade: '))
        soma = quantidade * 1
        
    if codigo == 3:
        quantidade = int(input('Digite a quantidade: '))
        soma = quantidade * 4
        
    if codigo == 5:
        quantidade = int(input('Digite a quantidade: '))
        soma = quantidade * 7
        
    if codigo == 9:
        quantidade = int(input('Digite a quantidade: '))
        soma = quantidade * 8
        
    else:
        print('Código invalido!')
    
print('Você irá pagar R$', soma)