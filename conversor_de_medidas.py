medida = float(input('Uma distancia em metros'))
cm = medida * 100
mm = medida * 1000
km = medida * 0.001
d = medida * 0.1
print('a medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
