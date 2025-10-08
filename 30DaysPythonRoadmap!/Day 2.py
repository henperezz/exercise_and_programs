#Day 2 - 30 days python roadmap

'''Há diversos tipos de funções integradas com o python, sem a necessidade
de configurar ou importar.'''

len('Hello World!')  #conta todos os caracteres da frase, incluindo espaços
type('Hello World!')  #checa o tipo do dado apresentado
str(10)  #converte número para string
int('10')  #converte para número
float(10)  #converte número inteiro para decimal
#input('Coloque seu nome: ')  #pega o que o usuário digitar
min(20, 30, 40, 50 ,10123)  #da o menor valor
max(20, 30, 40, 50, 10123)  #da o maior valor
min([20, 30, 40, 50])  #da o menor valor dentro de uma lista
max([20, 30, 40, 50])  #da o maior valor dentro de uma lista
sum([20, 30, 40, 50])  #da a soma dos valores, porém somente com listas
print('\n')  #escreve na tela seu conteúdo

'''Variáveis são dados armazenados na memória do computador, sendo que elas devem,
preferencialmente, ser nomes que sejam fáceis de lembrar. Há regras para definir uma variável,
sendo elas: Deve iniciar com uma letra ou underscore(_); Não pode começar com um número;
Só pode conter caractéres alpha-numéricos e underscores(_); Variáveis são sensíveis, ou seja,
abacate, Abacate e ABACATE são três variáveis diferentes.'''

primeiro_nome = 'Pedro'  #string
sobrenome = 'Perez'  #string
pais = 'Brasil'  #string 
cidade = 'Piracicaba'  #string
idade = 17  #int
e_casado = False  #bool 
habilidades = ['Python', 'Inglês', 'Matematica']  #list
informacoes_pessoais = {  #dict
    'primeironome':'Pedro',
    'sobrenome':'Perez',
    'pais':'Brasil',
    'Cidade':'Piracicaba'
}
print('\n')

#escrever o conteúdo das variáveis e seu tamanho

print('Primeiro nome:', primeiro_nome)
print('Número de caracteres:', len(primeiro_nome))
print('Sobrenome:', sobrenome)
print('Número de caracteres: ', len(sobrenome))
print('País:', pais)
print('Número de caracteres do país: ', len(pais))
print('Cidade:', cidade)
print('Números de caracteres da cidade:', len(cidade))
print('Idade:', idade)
print('É casado:', e_casado)
print('Habilidades:', habilidades)
print('Informações pessoais:', informacoes_pessoais)

print('\nÉ lindo?')
#É possível utilizar o comando input junto com uma variável

lindo = input('Sim ou não: ')
print('\n')

#verificação de tipos de dados

print(type(primeiro_nome))
print(type(sobrenome))
print(type(pais))
print(type(cidade))
print(type(idade))
print(type(e_casado))
print(type(habilidades))
print(type(informacoes_pessoais))
