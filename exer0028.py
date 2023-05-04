import random
from time import sleep

n = random.randint(1, 5)
print('-=-' *20)
print('Acerte o numero')
print('-=-' *20)
c = int(input('Acerte o numero gerado pelo programa: '))
print("PROCESSANDO...")
sleep(2)
if c == n:
    print('PARABENS! Você conseguiu me vencer!')
else:
    print('EU VENCI! O numero que eu pensei era {} e você digitou o {}'.format(n, c))