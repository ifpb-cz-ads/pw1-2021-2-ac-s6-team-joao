n = int(input('Digite o número da tabuada: '))
x = int(input('Digite o começo da tabuada: '))
m = int(input('Digite o fim da tabuada: '))

while x <= m:
	print(n,'x', x, '=', n * x)
	x = x + 1
