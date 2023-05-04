from datetime import date

ano_atual = date.today().year
pessoas = 0
n_m_idade = 0
for c in range(1, 8):
    nasc = int(input('Digite sua data de nascimento: '))
    idade = ano_atual - nasc
    if idade >= 18:
        pessoas = pessoas + 1
    else:
        n_m_idade = n_m_idade + 1
print('Um total de {} pessoas já são maiores de idade'.format(pessoas))
print('E um total de {} pessoas não são maiores de idade'.format(n_m_idade))