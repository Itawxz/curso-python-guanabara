from math import hypot
cateto_op = float(input('Digite o numero do cateto oposto: '))
cateto_ad = float(input('Digite o numero do cateto adjacente: '))
hipo = hypot(cateto_ad, cateto_op)
print('O valor da hipotenusa do triangulo é \033[31m{:.2f}'.format(hipo))
