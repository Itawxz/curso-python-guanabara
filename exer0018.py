from math import radians, sin, tan, cos
angulo = int(input('Digite o angulo para realizar o calculo: '))
cvr = radians(angulo)
seno = sin(cvr)
tangente = tan(cvr)
cosseno = cos(cvr)
print('O valor de {}'.format(angulo))
print('Seno: {:.2f}'.format(seno))
print('Tangente: {:.2f}'.format(tangente))
print('Cosseno: {:.2f}'.format(cosseno))
