produto = float(input('Digite o valor do produto'))
parcelado = produto + (produto*50/100)
p = parcelado / 12
print('O valor do produto a vista é de R${:.2f} \ne parcelado em 12x com a vicencia fica R${:.2f}\nCom parcelas fixas de R${:.2f}'.format(produto, parcelado, p))

