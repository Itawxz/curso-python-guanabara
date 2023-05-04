n1 = int(input('Digite um número para saber o fatorial: '))
f1 = 1
c1 = n1
while c1 > 1:
    f1 *= c1
    c1 -= 1
print('O fatorial de {}! é {}'.format(n1, f1))