medida = float(input('Uma distância em metro:'))
medida2 = float(input('Uma distância em metro:'))
cm = medida *100
mm = medida *1000
hm = medida *10
dam = medida *10.000
dm = medida * 100.000
km = medida * 1000.000
print('A medida de {}m corresponde a{:.0f}cm e {:.0f}mm '.format(medida, cm, mm))
print('A medida2 de  e {}hm corresponde a {}dam e {}dm e {}km '.format(hm, dam, dm, km))