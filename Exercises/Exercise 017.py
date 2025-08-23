from math import sqrt

cat1 = float(input('Digite o cateto oposto: '))
cat2 = float(input('Digite o cateto adjacente: '))

hipote = ((cat1**2)+(cat2**2))


print(f'A hipotenusa do triângulo retangulo é: {sqrt(hipote)}')