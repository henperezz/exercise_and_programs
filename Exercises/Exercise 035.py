reta1=float=input('Digite uam reta de um triângulo: ')
reta2=float=input('Digite uam reta de um triângulo: ')
reta3=float=input('Digite uam reta de um triângulo: ')


if reta1+reta2>reta3 and reta2+reta3>reta1 and reta3+reta1>reta2:
    print(f'é possível fazer um triângulo com as retas {reta1}, {reta2}, {reta3}')
else:
    print(f'Não é possível fazer um triângulo com as retas {reta1}, {reta2}, {reta3}')
