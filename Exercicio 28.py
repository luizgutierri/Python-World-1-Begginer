from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? >: '))
print('Hmmmmm.....')
sleep(2)
print(f'Acertou mizeravi, eu pensei no {computador}' if jogador == computador else f'Errou noob, o numero era {computador}, e nao {jogador}')
