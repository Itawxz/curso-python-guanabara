menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input('Digite o seu peso atual: '))
    if c == 1:
        maior += peso
        menor += peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido e de {} Kg'.format(maior))
print('O menor peso lido e de {} Kg'.format(menor))