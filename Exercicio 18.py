import math
angulo = float(input('Digite o angulo que voce deseja: '))
sen = math.sin(math.radians(angulo))
coss = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f'O angulo de {angulo:.1f} tem o SENO de {sen:.2f}')
print(f'O angulo de {angulo:.1f} tem o COSSENO de {coss:.2f}')
print(f'O angulo de {angulo:.1f} tem o TANGENTE de {tan:.2f}')
