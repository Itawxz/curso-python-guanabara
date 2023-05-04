n = int(input('Primeiro termo: '))
n2 = int(input('Razao: '))
decimo = n + (10 - 1) * n2
for c in range(n, decimo + n2, n2):
    print(c, end=' > ')
print('ACABOU')