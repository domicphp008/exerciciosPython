#======Desafio 012==========================
#====Aula 07 - Calculando Descontos (%)=====

#===R$10      100%


#===x           5%

#===========================================


preço = float(input('Qual é o preço do produto? R$'))
novo =  preço - (preço * 3.2/100)
print('O produto que custava R${:.2f}, na promoção com desconto de 3.2% vai custar R${:.2f}'.format(preço, novo))



