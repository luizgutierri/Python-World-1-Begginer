distancia = int(input(f'Qual a distancia em KMs da sua viagem: '))
print(f'Voce esta prestes a comecar uma viagem de {distancia:.1f}Km!')
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O preco da sua passagem sera de R${preco:.2f}')
