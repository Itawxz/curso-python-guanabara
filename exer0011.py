alt = float(input('Qual a altura do quarto: '))
lar = float(input('Qual a largura do quarto: '))
area = lar * alt
print('A areá do quarto é de {} metros.'.format(area))
tinta = area / 2
print('Vocé precisa de \033[36m{}\033[m litros para pintar o quarto.'.format(tinta))