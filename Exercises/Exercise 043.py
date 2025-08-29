peso=float(input('Digite seu peso: '))
altura=float(input('Digite sua altura em metros: '))

imc= peso/(altura**2)

print(f'Seu IMC é de {imc:.2f}')

if imc<18.5:
    print('Abaixo do peso!')
elif imc<25:
    print('Peso normal!')
elif imc<30:
    print('Acima do peso!')
elif imc<40:
    print('Obesidade!')
else:
    print('Obesidade mórbida')
