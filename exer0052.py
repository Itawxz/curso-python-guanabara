num = int(input('Digite um numero: '))
v = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
        v += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi dividido {} vezes'.format(num, v))
if v == 2:
    print('E por isso ele e PRIMO')
else:
        print('E por isso ele não e PRIMO')