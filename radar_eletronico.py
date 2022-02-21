v = float(input('Qual é a velocidade do carro? '))
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h!')
    m = (v - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(m))
else:
    print('Tenha um bom dia, dirija com segurança!')
