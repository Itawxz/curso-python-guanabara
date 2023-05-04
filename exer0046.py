from time import sleep

for c in range(10, -1, -1):
    print('Em {} segundos os fogos serão estourados'.format(c))
    sleep(1)
print('Fogos de artificio estourados!')