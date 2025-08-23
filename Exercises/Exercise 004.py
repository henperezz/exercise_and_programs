#Faça um programa que disseque uma variável
algo=input('Digite algo: ')

print('Qual seu tipo primitivo? ', type(algo))
print('Só tem espaços? ', algo.isspace())
print('É um número? ', algo.isnumeric())
print('É alfabético? ', algo.isalpha())
print('É alfanumérico? ', algo.isalnum())
print('Está em maiúsculas? ', algo.isupper())
print('Está em minúsculas? ', algo.islower())
print('Está capitalizada? ', algo.istitle())