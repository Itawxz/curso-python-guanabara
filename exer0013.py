salario = float(input('Qual é o seu salario: '))
porcentagem = salario * 15 / 100
print(porcentagem)
aumento = salario + porcentagem
print('\033[33mParabens! Esse mês vocé teve um aumento de R${:.2f} reais!\nSalario antes do aumento: R${:.2f} reais.\nDepois do aumento: R${:.2f} reais.'.format(porcentagem, salario, aumento))