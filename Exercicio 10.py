cash = float(input('Quanto dinheiro voce tem na carteira: '))
dolar = 3.27
convertido = cash / dolar

print(f'Com R${cash:.2f} voce pode comprar: U${convertido:.2f}')
