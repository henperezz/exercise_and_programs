n1=float(input('Digite um número: '))
n2=float(input('Digite um número diferente: '))
n3=float(input('Digite um número diferente: '))

if n1>n2 and n1>n3 and n2>n3:
    print(f'O maior e o menor número são: {n1} e {n3} ')
elif n2>n1 and n2>n3 and n1>n3:
    print(f'O maior e o menor número são: {n2} e {n3}')
else:
    print(f'O maior e o menor número são: {n3} e {n1}')