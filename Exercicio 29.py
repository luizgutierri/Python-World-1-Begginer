velocidade = float(input('Qual a velocidade do seu carro? '))
if velocidade > 80:
    print('MULTADO! Voce excedeu o limite permitido: 80KM/h')
    multa = (velocidade-80) * 7
    print(f'Voce deve pagar uma multa de R${multa:.2f}')
print('Tenha um bom dia, dirija com cuidado!')




