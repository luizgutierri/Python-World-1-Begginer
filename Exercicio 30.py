numero = float(input('Digite um numero, para saber se e par ou impar: '))
resto = numero % 2

if resto == 0:
    print(f' O numero {resto:.0f} e PAR!')
else:
    print(f'O numero {resto:.0f} e IMPAR!')

