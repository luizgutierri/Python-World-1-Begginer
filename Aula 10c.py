n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digita a sua segunda nota: '))
m = (n1 + n2)/2
print(f'A sua media foi {m:.1f}!!')
print(f'Parabens a nota {m} foi otima!' if m >= 5 else f'Sua nota foi {m}, uma bosta, estude mais!')

