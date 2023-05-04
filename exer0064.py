n = 0
s = 0
c = 0
n = int(input('Digite um numero: [999 para parar] '))
while n != 999:
    c = c + 1
    s = s + n
    n = int(input('Digite um numero: [999 para parar] '))
print('Você digitou {} numeros e a soma entre eles é de {}'.format(c, s))
