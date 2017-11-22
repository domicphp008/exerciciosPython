#========Desafio 011 Calculando área por  m²#

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimesão de {:.2f} x {:.2f} e sua áre é de {}m². '.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede você precirá de {}l de tinta.'.format(tinta))