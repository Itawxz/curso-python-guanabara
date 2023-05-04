n = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite a razao: '))
decimo = n + (10 - 1) * n2
print(decimo)
a = 0
c = 0
b = 0
while a < 10:
    a = a + 1
    print(c, end=' > ')
    c = n + n2 * a
print('ACABOU')