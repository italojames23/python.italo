from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))
print('processando...')
sleep(3)
if jogador == computador:
    print('PARABÉNS ! Você consegui me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))
