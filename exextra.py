#====== Trabalhando com Porcentagem ======
#======  Aqui estou procurando o a porcentagem em si % ======

emprestimo = float(input('Valor do meu empréstimmo é: R$'))

preço = float(input('Valor do juro por mês: R$'))
novo =  2000 /preço
print('Pago por mes  R${:.2f}\nNo percentual cobrado de{:.2f}%'.format(preço,novo))

