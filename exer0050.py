import time

soma = 0
cont = 0
for c in range(0, 6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Somando..')
time.sleep(1)
print('Você informou {} Numeros PARES e soma resultou em {}'.format(cont, soma))
