from datetime import date

ano_atual = date.today().year
nascimento = int(input('Em que ano você nasceu?\nResponda: '))
alistamento = nascimento + 18
if alistamento > ano_atual:
    a = alistamento - ano_atual
    print('\033[0;32mALISTAMENTO! Ainda Falta {} anos para você se alistar!'.format(a))
elif alistamento == ano_atual:
    print('\033[0;32mALISTAMENTO! Parece que você está na idade para se alistar!')
elif alistamento < ano_atual:
    a = ano_atual - alistamento
    print('\033[0;31mALISTAMENTO! Você está {} anos atrasado para o alistamento!'.format(a))