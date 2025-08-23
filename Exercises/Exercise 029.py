velo=float(input('Digite a velocidade registrada: '))

if velo>80:
    multa=(velo-80)*7
    print(f'Você está acima do limite permitido, sua multa será de R${multa:.2f} ')
else:
    print('Velocidade permitida! Sem multa aplicada.')