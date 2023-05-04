from random import choice

print('=-='*10)
print('     PEDRA PAPEL TESOURA')
print('Divirta-se com o script')
print('=-='*10)
p = ['pedra', 'papel', 'tesoura']
jogue = int(input('Escolha qual uma alternativas abaixo\n1) Pedra\n2) Papel\n3) Tesoura\nJogue: '))
a = choice(['pedra', 'papel', 'tesoura'])
if jogue == 1:
    if a == 'pedra':
        print('TENTE NOVAMENTE! Você escolheu o mesmo do programa jogue novamente!')
    elif a == 'papel':
        print('PERDEDOR! O programa venceu você!')
    elif a == 'tesoura':
        print('VENCEDOR! Você ganhou o programa escolheu "TESOURA"')
if jogue == 2:
    if a == 'pedra':
        print('VENCEDOR! Você ganhou o programa escolheu "PEDRA"')
    elif a == 'papel':
        print('TENTE NOVAMENTE! Você escolheu o mesmo do programa jogue novamente!')
    elif a == 'tesoura':
        print('PERDEDOR! O programa venceu você!')
if jogue == 3:
    if a == 'pedra':
        print('PERDEDOR! O programa venceu você!')
    elif a == 'papel':
        print('VENCEDOR! Você ganhou o jogo! O programa escolheu PAPEL!')
    elif a == 'tesoura':
        print('TENTE NOVAMENTE! Você escolheu o mesmo do programa jogue novamente!')
print('''
O programa escolheu {}'''.format(a))