# Salario menor que 9000 ganha 10% acima de 9000 gannha 15% de aumento
salario = int(input('Qual seu salario: R$'))

if salario <= 1250:
    aumento = salario * 1.15
else:
    aumento = salario * 1.10

print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora')
