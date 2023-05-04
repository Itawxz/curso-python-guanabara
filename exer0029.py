v = int(input('Você está em qual velocidade em seu carro: '))
if v > 80:
    print('Você ultrapassou a velocidade')
    m = (v - 80) * 7
    print('O valor da multa será de {:.2f} Reais'.format(m))
print('Tenha um bom dia dirija com segurança')