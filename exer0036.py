print('''\033[1;36m
       CALCULE SEU FINANCIAMENTO
Este programa foi criado para que os usuarios calculem seu financiamento.

''')
valor_da_casa = float(input('\033[1;32mQual o valor da casa?\nResponda:'))
salario = float(input('Qual é o seu salario?\nResponda: '))
qntd_anos = int(input('Em quantos anos você vai pagar?\nResponda: '))

parcelas = 12 * qntd_anos
prestacao = valor_da_casa / parcelas
salario_porcento = salario * 30 / 100
if prestacao < salario_porcento:
    print('''
    PARABENS! Seu financiamento foi aprovado\n    Valor da Parcela: {:.2f}\n    Qntd de Parcelas: {}'''.format(prestacao, parcelas))
elif prestacao > salario_porcento:
    print('''
    \033[4;31mPEDIDO NEGADO!\033[0;30m
    \033[0;31mInfelizmente você não pode financiar está casa!''')
