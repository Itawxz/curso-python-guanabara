print('''
       CALCULO IMC
MENOR QUE 18,5	MAGREZA	0
ENTRE 18,5 E 24,9	NORMAL	0
ENTRE 25,0 E 29,9	SOBREPESO	I
ENTRE 30,0 E 39,9	OBESIDADE	II
MAIOR QUE 40,0	OBESIDADE GRAVE	III

''')
peso = float(input('Qual é o seu peso atual? '))
altura = float(input('Qual a sua altura atual? '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print('CUIDADO! Você está ABAIXO DO PESO IDEAL!')
elif imc <= 25:
    print('Você está no seu PESO IDEAL')
elif imc <= 30:
    print('CUIDADO! Você está com SOBRE PESO')
elif imc <= 40:
    print('MUITO CUIDADO! Você está com OBESIDADE')
else:
    print('URGENCIA!! Você está com OBESIDADE MORBIDA procure um MEDICO')