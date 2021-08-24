altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
area = largura * altura
tinta = area / 2

print(f'Sua parede tem a dimensao de {altura}m x {largura}m e sua area vale {area}m².')
print(f'Para pintar essa parede voce precisara de {tinta}l de tinta.')
