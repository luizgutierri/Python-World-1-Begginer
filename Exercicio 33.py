a = int(input('Digite um numero: '))
b = int(input('Digite um segundo numero: '))
c = int(input('Digite um terceiro numero: '))
menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'Menor numero: {menor}')
print(f'Maior numero: {maior}')

