'''n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))'''
'''while e != 0:'''
e = 10
while e != 5:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    print('''Qual das opções abaixo você vai escolher: 
     [1] somar
     [2] multiplicar
     [3] maior numero
     [4] novos numeros
     [0] sair do programa''')
    e = int(input('Escolha uma opção: '))
    if e == 5:
        print('Fechando o programa')
        e = 5
    if e == 1:
     s = n1 + n2
     print('A soma de {} + {} resulta em {}'.format(n1, n2, s))
    if e == 2:
        s = n1 * n2
        print('A multiplicação de {} por {} resulta em {}'.format(n1, n2, s))
    if e == 3:
        if n1 > n2:
            print('O maior numero é {}'.format(n1))

        if n2 > n1:
            print('O maior numero é {}'.format(n2))
    if e == 4:
        print('DIGITE OS NUMEROS DENOVO!!')