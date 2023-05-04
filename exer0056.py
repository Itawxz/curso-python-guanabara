nomes = ''
idades = 0
sexos = ''
mulheres = 0
media = 0
for pesso in range(1, 5):
    print('-----{}ª PESSOA-----'.format(pesso))
    nome = str(input('Qual é seu nome: '))
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Sexo: [M/F] '))
    media = media + idade
    if pesso == 1:
        nomes += nome
        idades += idade
        sexo += sexo
    else:
        if idade > idades and sexo == 'M':
            idades = idade
            nomes = nome
        elif sexo == 'F' and idade <= 20:
            mulheres = mulheres + 1
m = media / 4
print('A media de idade do grupo é {:.0f} anos'.format(int(m)))
print('O homem mais velho do grupo tem {} anos e se chama {}'.format(idades, nomes))
print('No grupo tem {} mulheres com menos de 20 anos'.format(mulheres))