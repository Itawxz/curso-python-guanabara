r1 = float(input('Digite os metros de um lado do triangulo: '))
r2 = float(input('Digite os metros do outro lado do triangulo: '))
r3 = float(input('Digite os metros do outro lado tambem: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('E possivel formar um triangulo')
    if r1 == r2 == r3:
        print('Esse triangulo e Equilatero')
    #elif r1 == r2 != r3 or r1 != r2 == r3 or r1 == r3 != r2:
        #print('Esse triangulo e Isosceles')
    elif r1 != r2 != r3 != r1:
        print('Esse triangulo e escaleno')
    else:
        print('Esse triangulo e Isosceles')
else:
    print('Não foi possivel formar um triangulo')