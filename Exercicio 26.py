frase = str(input('Digite uma frase:')).strip().lower()
count = frase.count('a')
apos = frase.find('a')
rapos = frase.rfind('a')

print(f'A letra A aparece {count} vezes na frase.')
print(f'A primeira letra A apareceu na posicao {apos}')
print(f'A ultima letra A apareceu na posicao {rapos}')


