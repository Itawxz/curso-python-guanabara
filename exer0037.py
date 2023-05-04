print('CONVERSOR DE NUMEROS!')
print('*' * 20)
numero = int(input('Digite um numero: '))
tipo_conv = int(input('Qual o tipo da conversão? \n1) Binario.\n2) Octal\n3) Hexadecimal\nEscolha: '))
if tipo_conv == 1:
    print('O Numero binario de {} é o {}'.format(numero, bin(numero)[2:]))
elif tipo_conv == 2:
    print('O numero octal de {} é o {}'.format(numero, oct(numero)[2:]))
elif tipo_conv == 3:
    print('O numero hexadecimal de {} é o {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida! Tente Novamente')
