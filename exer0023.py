numero = int(input('Digite um numero: '))
if numero > 9999:
    print('Digite um numero menor que 9999')
else:
    u = numero // 1 % 10
    d = numero // 10 % 10
    c = numero // 100 % 10
    m = numero // 1000 % 10
    st = str(numero)
    print('Unidade: {}'.format(u))
    print('Dezena: {}'.format(d))
    print('Centena: {}'.format(c))
    print('Milhar: {}'.format(m))