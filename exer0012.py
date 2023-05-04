valor = float(input('Qual o valor do produto: '))
desconto = valor * 5 / 100
novo_valor = valor - desconto
#print('O valor descontado será R${} reais.'.format(novo_valor))
print('O produto que custava R$\033[31m{:.2f}\033[m com o desconto de 5% agora vale R$\033[33m{:.2f}\033[m'.format(valor, novo_valor))