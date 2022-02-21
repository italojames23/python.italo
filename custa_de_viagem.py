distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(distancia))
if distancia >= 200:
    print('E o preço da sua passagem é de {:.2f}'.format(distancia * 0.45))
else:
    print('E o valor da sua passagem é {:.2f}'.format(distancia * 0.50))
