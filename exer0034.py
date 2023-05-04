salario = float(input('Qual é o seu salario atual: '))
if salario <= 1250:
    aumento = salario + (15 * salario / 100)
else:
    aumento = salario + (10 * salario / 100)
print('Seu salario agora é: {}'.format(aumento))