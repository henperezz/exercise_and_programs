from random import randint

jogador=int(input('Digite um numero de 0 a 5: '))
computador= randint(0,5)

if jogador==computador:
    print('Você acertou!')
else:
    print('Você errou!')