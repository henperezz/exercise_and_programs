#Faça um programa que leia o valor e mostre o seu triplo, duplo e raiz quadrada

num=int(input('Digite um valor: '))

tri=num*3
dup=num*2
rzq=num**(1/2)

print(f'O duplo, triplo e raiz de {num} são respectivamente: {dup} {tri} {rzq:.2f}')