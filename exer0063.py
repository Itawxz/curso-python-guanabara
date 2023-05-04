print('='*20)
print('SEQUENCIA DE FIBONNACI')
print('='*20)
n = int(input('Digite o termo: '))
t1 = 0
t2 = 1
count = 3
print('{} > {}'.format(t1, t2), end='')
while count <= n:
    count = count + 1
    t3 = t1 + t2
    print(' > {}'.format(t3), end='')
    t1 = t2
    t2 = t3
print(' > ACABOU')
print('='*20)