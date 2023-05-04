frase = str(input('Digite uma frase: ')).replace(' ', '').upper()
a = frase[::-1]
if frase == a:
    print('A frase "{}" é do tipo palindromo'.format(frase))
else:
    print('A frase "{}" não é do tipo palindromo'.format(frase))