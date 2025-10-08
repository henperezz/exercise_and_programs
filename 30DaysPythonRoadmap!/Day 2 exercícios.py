'''Exercícios level 1- declare 11 variáveis diferentes, sendo elas:Primeiro nome; Último nome;
Nome completo; País; Cidade; Idade; Ano; É casado; is_true; is_light_on; Múltiplas variáveis
em uma linha. '''

first_name = 'Pedro Henrique'  # str
last_name = 'Perez'  # str
full_name = 'Pedro Henrique Perez'  # str
country = 'Brasil'  # str
age = 17  # int
year = 2025  # int
is_married = False  # bool
is_true = True  # bool
is_light_on = False  # bool
fav_color, fav_volleyball_position, fav_subject = 'Green', 'Setter', 'Math'  # str str str
print('\n')

'''Exercícios level 2- Cheque o tipo de dados de todas as variáveis; Conte a quantidade de caracteres da variável |first_name| e compare-a com |last_name|;
declare as variáveis |num_one| e |num_two| como 5 e 4 respectivamente; Faça todas as operações com essas variáveis; calcule a área e a circunferencia de um circulo de raio de 30 metros;
calcule a área de um circulo com o raio dado pelo usuário; Peça ao usuário o primeiro nome, ultimo nome, país e idade e guarde suas informações em variáveis respectivas.'''

print(type(first_name))  # should return str
print(type(last_name))  # should return str
print(type(full_name))  # should return str
print(type(country))  # should return str
print(type(age))  # should return int
print(type(year))  # should return int
print(type(is_married))  # should return bool
print(type(is_true))  # should return bool
print(type(is_light_on))  # should return bool
print(type(fav_color))  # should return str
print(type(fav_volleyball_position))  # shoudl return str
print(type(fav_subject))  # should return str
print(len(first_name))
print(len(first_name), len(last_name))
print('\n')

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one * num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
print('\n')

area_aproximada = 3.14 * (30**2)
circunferencia_aproximada = 2 * 3.14 * (30**2)

print('Área: ', area_aproximada, 'Circunferência:', circunferencia_aproximada)
print('\n')

raio = int(input('Digite o raio de uma circunferência: '))

area_aprox_usuario = 3.14 * (raio ** 2)

print('Área:', area_aprox_usuario)
print('\n')

user_first_name = input('Digite seu primeiro nome: ')
user_last_name = input('Digite seu último nome: ')
user_country = input('Digite seu país: ')
user_age = int(input('Digite sua idade: '))
print('\n')

help('keywords')