# Exercico Python #017=============
#=========Catetos e Hipotenusa======
#==============Desafio=============
#=================================="

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adiacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
