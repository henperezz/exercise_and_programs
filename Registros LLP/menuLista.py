#definição de variáveis
lista_de_compras= []
opcao = 0

#laço de repetição para o usuário fazer suas ações
while opcao != 4:
    print(f'{'Lista de compras':=^40}')
    print('''1- Adicionar item
2- Remover item
3- Ver lista
4- Sair''')
    print('='*40)
    opcao = int(input('Digite a ação: '))

#estrutura para realizar as ações

    if opcao == 1:
        item = input('Digite o item a ser adicionado: ')
        lista_de_compras.append(item)
    elif opcao == 2:
        if lista_de_compras == 0:
            print('A lista está vazia! Adicione algo para remover')
        else:
            for index, item in enumerate(lista_de_compras):
                print(index, item)
            index = int(input('Digite o número do item a ser removido: '))
            lista_de_compras.pop(index)
            print(f'O item de número {index}, foi removido!')

    elif opcao == 3:
        for index, item in enumerate(lista_de_compras):
            print(index, item)
    elif opcao ==4:
        print('Saindo')
    else:
        print('Número inválido digitado, tente novamente')
        