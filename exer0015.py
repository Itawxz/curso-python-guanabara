dias = int(input('Quantos dias vocé alugou o carro: '))
quilometros = float(input('E quantos km vocé rodou com o carro: '))
pagar = (dias * 60) + (quilometros * 0.15)
print('\033[33mO total a pagar é de R${:.2f} reais'.format(pagar))