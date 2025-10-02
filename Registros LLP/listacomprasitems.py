#lista de compras - adiciona itens
#criando uma lista vazia
lista_compras=[]

#laço de repetição e estrutura de funcionamento do código

while True:
    produto = input('Digite o nome do produto selecionado (ou "sair" para encerrar): ')

    if produto.lower() == 'sair':
        break
    
    lista_compras.append(produto)#adicionar item na lista
    
    print('\n Lista de compras:')
    for index, item in enumerate(lista_compras, start=1):
        print (index, '-', item )