lado1=float(input('Digite um número: '))
lado2=float(input('Digite um número: '))
lado3=float(input('Digite um número: '))

if (lado1+lado2)<lado3 or (lado2+lado3)<lado1 or (lado3+lado1)<lado2:
    print('Não é possível fazer um triângulo')
else:
    if lado1==lado2==lado3:
        print('É possível fazer um triângulo Equilátero!')
    elif lado1==lado2 or lado2==lado3 or lado1==lado3:
        print('É possível fazer um triângulo Isósceles')
    else:
        print('É possível fazer um triângulo Escaleno!')