nome = str(input('Digite seu nome')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome eo minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))