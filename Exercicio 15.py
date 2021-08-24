kmcorridos = float(input('Quantos Kms foram percorridos? '))
diasdeuso = float(input('Quantos Dias ficou com o carro? '))
valorpordia = 60.00
valorporkm = 0.15

print(f'O valor do seu aluguel ficou em R${(kmcorridos * valorporkm) + (diasdeuso * valorpordia):.2f}')
