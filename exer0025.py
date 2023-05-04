nome = input('Digite seu nome: ')
n = nome.upper()
if 'SILVA' in n:
    print('O nome Silva foi encontrado em {}'.format(nome))
else:
    print('O nome Silva não foi encontrado em {}'.format(nome))