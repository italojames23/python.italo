real = float(input('Quanto dinheiro você tem na carteira?'))
dolar = real / 3.27
print('Com R${} você pode comprar us${:.2f}'.format(real, dolar))
