real = float(input('A quanto em dinheiro você tem na carteira? R$'))
dolar = real / 3.2750
euro  = real / 3.79
print('Com R${} você pode comprar US${:.4f} em euro € {:.4f}'.format(real, dolar, euro))
