'''Exercício level 1/2 - execute todas as operações com os operandos 3 e 4
escreva comandos str sobre: seu nome; seu sobrenome; seu país; eu estou aproveitando os primeiros 30 dias de python
verifique os seguintes tipos de dados: 10 ; 9.8; 3.14; 4 - 4j; ['Pedro', 'Python', 'Finland']; seu nome; seu sobrenome; seu país'''

print(3 - 4)  #subtração
print(3 + 4)  #adição
print(3 * 4)  #multiplicação
print(3 / 4)  #divisão
print(3 ** 4)  #exponenciação
print(3 // 4)  #divisão inteira
print(3 % 4)  #módulo

print('Pedro Henrique')  #nome
print('Perez')  #sobrenome
print('Brasil')  #país que moro
print('Eu estou aproveitando os primeiros 30 dias de python')  #frase predefinida

print(type(10))  #int
print(type(9.8))  #float
print(type(3.14))  #float
print(type(4 - 4j))  #complex
print(type(['Pedro', 'Python', 'Finland']))  #list
print(type('Pedro Henrique'))  #str
print(type('Perez'))  #str
print(type('Brasil'))  #str

'''Exercício level 3- escreva diferentes tipos de exemplos para os seguintes
tipos de dados em python: Inteiro, Flutuante, Complexo, Strings, Booleanos, Listas, Tuplas, Set e Dicionário.
Ache a distância Euclidiana entre (2,3) e (10,8)'''

print('\n')

print(type(350))  #int
print(type(2.4))  #float
print(type(2 + 8j))  #complex
print(type(False))  #bool
print(type([8, 3, 2, 1, 24]))  #list
print(type(('Pedro', 'Henrique', 'Perez', 'É', 'Bobo')))  #tuplas
print(type({1, 2, 6}))  #set
print(type({'Duas':'Frases'}))  #dict

print('\n')

ponto1= 2, 3  #definição do ponto 1
ponto2= 10, 8  #definição do ponto 2

x= 10-2  #achar o ponto x
y= 8-3  #achar o ponto y

p_sqr = (x**2) + (y**2)  #elevar os pontos x e y ao quadrado e somá-los

p_root = p_sqr**0.5  #tirar a raiz quadrada da soma

print(p_root)  #escrever o resultado