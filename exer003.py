n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
print('A soma de \033[33m{} \033[0;32m+ \033[0;34m{} \033[mresulta em \033[31m{}'.format(n1, n2, s))