valor_prod = float(input('\033[1;34mDigite o valor do produto: '))
d_cheque_avista =  valor_prod - ((valor_prod * 10) / 100)
a_cartao = valor_prod - ((valor_prod * 5) / 100)
juros = valor_prod + (valor_prod * 20 / 100)
print(d_cheque_avista)
condicao_pag = int(input('Qual a condição do pagamento? \n1) A vista com cheque (10% de desconto)\n2) A vista no cartão (5% de desconto)\n3) 2X no cartão preço normal\n4) 3x ou mais no cartão (20% de juros)\nResponda: '))
if condicao_pag == 1:
    print('CHEQUE ESPECIAL')
    print('O valor a ser pago com o cheque será de R${:.2f} reais'.format(d_cheque_avista))
elif condicao_pag == 2:
    print('A VISTA NO CARTÃO')
    print('O valor a ser pago com o cartão será de R${:.2f} reais'.format(a_cartao))
elif condicao_pag == 3:
    print('2X NO CARTÃO')
    print('O valor a ser pago parcelado em 2X será de R${:.2f} reais'.format(valor_prod))
elif condicao_pag == 4:
    parc = int(input('Quantas parcelas: '))
    parcela = juros / parc
    print('{}X NO CARTÃO (20% de Juros)'.format(parc))
    print('O valor a ser pago de R${:.2f} reais parcelado em {}X vezes será de R${:.2f} com juros'.format(juros, parc, parcela))
else:
    print('Opção invalida. Tente Novamente')