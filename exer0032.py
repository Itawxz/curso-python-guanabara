from datetime import date

ano = int(input('Que ano quer analisar: '))
c = ano % 4
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} BISSEXTO'.format(ano))
else:
    print('O ano {} não e um ano É BISSEXTO'.format(ano))