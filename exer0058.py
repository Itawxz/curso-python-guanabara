import random
c = 0
p = 0
g = random.randrange(1, 11)
while c != g:
    c = int(input('Chute um numero: '))
    if c == g:
        print('PARABENS! Você acertou')
    else:
        p = p + 1
        print('ERROU! Tente novamente')
print('Você palpitou {} vezes, ate acertar'.format(p))