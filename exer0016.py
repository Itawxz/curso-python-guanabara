from math import trunc

num = float(input('Digite um numero: '))
print('\033[33mO numero digitado é \033[31m{:.2f} \033[33me tem a parte inteira \033[31m{}'.format(num, trunc(num)))