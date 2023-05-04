km = int(input('Quantos quilometros será a sua viagem: '))
if km >= 200:
    valor = km * 0.45
else:
    valor = km * 0.50
print('O valor da passagem é R${:.2f} reais.'.format(valor))