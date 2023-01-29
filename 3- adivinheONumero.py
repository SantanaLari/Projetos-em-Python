from random import randint

pc = randint(1, 100)
palpite = 0
tentativas = 0

if pc % 2 == 0:
    pista = 'par'
else:
    pista = 'impar'

print('Vamos jogar um jogo de adivinhação. '
      '\nEu penso em um número entre 1 e 100 e você tenta descobrir qual é.'
      '\nMas não se preocupe, se você errar, eu te digo se o número que você pensou é '
      '\nmaior ou menor que o número que eu pensei')

while palpite != pc:
    palpite = int(input('Digite seu palpite: '))

    if palpite > pc:
        print('O número que eu pensei é menor do que', palpite)
        tentativas += 1
    elif palpite < pc:
        print('O número que eu pensei é maior do que', palpite)
        tentativas += 1
    else:
        print('Você acertou! Eu pensei no número', pc)
        tentativas += 1

    if tentativas == 5:
        print('Estou vendo que você está com dificuldades para descobrir.'
              '\nAqui vai uma pista: O número que eu pensei é ', pista)

print(f'Você teve um total de: {tentativas} tentativas')
