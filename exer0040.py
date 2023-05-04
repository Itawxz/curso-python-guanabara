n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('\033[1;31mREPROVADO! A sua media foi {} e ficou abaixo de 5!'.format(media))
elif media < 6.9:
    print('\033[1;33mRECUPERAÇÃO! Sua media foi de {} E Você bateu na trave.. quase foi reprovado ficou de recuperação!'.format(media))
elif media > 7:
    print('\033[1;32mAPROVADO! Sua media foi de {} Parabens por manter suas notas altas você passou diretooo'.format(media))