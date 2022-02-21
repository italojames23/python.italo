import random
from time import sleep
nome = str(input('Olá, qual é o seu nome? '))
print('Olá {}, seja bem vindo ao nosso canal de jogos!!'.format(nome))
jogo = str(input('{}, sorteamos um jogo legal para que você conheça um pouco sobre a nossa plataforma de games, o jogo do dado. Você gostaria de conhecer esse jogo? '.format(nome)))
if jogo == ('sim' and 'Sim' and 'SIM'):
    print('Que legal, vamos começar a se divertir!!!')
    sleep(1)
    adv = str(input('Qual numero você acha que vai cair? '))
    print('Jogue o dado {}!'.format(nome))
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista = random.choice(lista)
    sleep(2)
    print('jogando dado...')
    sleep(3)
    if adv == lista:
        print('O dado caiu com o numero {} virado para cima, você acertou!'.format(lista))
    else:
        print('Que pena, você errou, tente me superar!!!')
else:
    print('Tudo bem, volte outra hora que estarei aqui para brincarmos!!')



