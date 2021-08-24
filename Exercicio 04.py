a = input('Digite algo: ')
print(f'O tipo primitivo desse valor e {type(a)}')
print('So tem espacos?', a.isspace())
print('E um numero?', a.isnumeric())
print('E alfabetico?', a.isalpha())
print('E alfanumero?', a.isalnum())
print('E maisculo?', a.isupper())
print('E minusculo?', a.islower())
print('E capitalizada?', a.istitle())


