n = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite a razao: '))
decimo = n + (10 - 1) * n2
a = 0
c = 0
b = 0
z = 0
while a < 10:
    a = a + 1
    print(c, end=' > ')
    c = n + n2 * a
print('ACABOU')
print('''
Você quer mostrar mais termos:
[1] Sim
[2] Não''')
s = int(input('Escolha: '))
if s == 1:
    q = int(input('Quantos termos: '))
    while z < q:
        z = z + 1
        k = c + n2 * z
        print(k, end=' > ')
    print('ACABOU')
    if q == 0:
        print('Parando..')
elif s == 2:
    print('Encerrando..')
else:
    print('Opção invalida!')