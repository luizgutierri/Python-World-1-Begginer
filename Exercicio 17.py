import math
cco = float(input('Comprimento do cateto oposto: '))
cca = float(input('Comprimento do cateto adjacente: '))
hip = math.hypot(cco, cca)

print(f'A hipotenusa vai medir {hip:.2f}')
