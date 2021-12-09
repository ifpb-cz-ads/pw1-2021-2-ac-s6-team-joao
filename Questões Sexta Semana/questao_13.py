numero = 1
soma = 0
media = 0
contagem = 0

while numero != 0:
    
    numero = 0
    numero = int(input('Digite um numero: '))
    
    if(numero != 0):
        soma = soma + numero
        contagem = contagem + 1
    

media = soma / contagem
    
print('A soma dos números é:', soma)
print('A média dos números é:', media)