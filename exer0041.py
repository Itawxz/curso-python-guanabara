from datetime import date

ano_atual = date.today().year
ano_nasc = int(input('Em qual ano você nasceu? '))
idade = ano_atual - ano_nasc
print(idade)
if idade <= 9:
    print('Você tem {} anos e sua categoria e de nivel: MIRIM'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e sua categoria e de nivel: INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e sua categoria e de nivel: JUNIOR'.format(idade))
elif idade <= 20:
    print('Você tem {} anos e sua categoria e de nivel: SÊNIOR'.format(idade))
else:
    print('Você tem {} anos e sua categoria e de nivel: MASTER'.format(idade))