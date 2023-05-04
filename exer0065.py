sidi = 'S'
n = v = c = menor = maior = quant = 0
while sidi == 'S':
    v = v + 1
    n = int(input('Digite algum numero: '))
    c = c + n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    sidi = str(input('Quer continuar: S/N ')).upper()
media = c / v
print('A sua media foi de {}'.format(media))
print('O maior numero foi {} e o menor numero foi {}'.format(maior, menor))