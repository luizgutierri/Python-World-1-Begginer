print('\033[1:32m-='*20)
print('Analisador de triangulos')
print('-='*20)
SegA = float(input(f'\033[mSegmento 1: '))
SegB = float(input('Segmento 2: '))
SegC = float(input('Segmento 3: '))

if SegA < SegB + SegC and SegB < SegA + SegC and SegC < SegA + SegB:
    print(f'\033[35mOs segmentos acima podem formar um Triangulo')
else:
    print('Os segmentos acima nao podem formar um Triangulo\033[35m')
