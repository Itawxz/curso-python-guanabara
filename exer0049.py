"""print('\033[35m='*30)
print(' '* 10, 'TABUADA')
print('='*30)
valor = int(input('Digite um valor: '))
print(valor, 'X 1 =', valor * 1)
print(valor, 'X 2 =', valor * 2)
print(valor, 'X 3 =', valor * 3)
print(valor, 'X 4 =', valor * 4)
print(valor, 'X 5 =', valor * 5)
print(valor, 'X 6 =', valor * 6)
print(valor, 'X 7 =', valor * 7)
print(valor, 'X 8 =', valor * 8)
print(valor, 'X 9 =', valor * 9)
print(valor, 'X 10 =', valor * 10)"""
print('-='* 11)
print('TABUADA')
print('-='* 11)
n = int(input('Digite um numero: '))
for c in range(1, 11):
    #print(c)
    print(n, 'X', c, '=', n * c)
print('FIM DA TABUADA')
