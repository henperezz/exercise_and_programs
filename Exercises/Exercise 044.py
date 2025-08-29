print(f'{'Loja Amendoeira':=^40}')
valor = float(input('Digite o valor de sua compra: R$'))
pagamento = int(input('''FORMA DE PAGAMENTO: 
[1] A vista no dinheiro/cheque
[2] A vista no cartâo
[3] Até 2x no cartâo
[4] 3x ou mais no cartão
[5] Sair
'''))

if pagamento == 1:
    print('O método de pagamento selecionado oferece um desconto de 10%!')
    desconto = valor*(10/100)
    valorfinal = valor-desconto
    print(
        f'O valor da compra inicial de R${valor} foi descontado para R${valorfinal:.2f}')
elif pagamento == 2:
    print('O método de pagamento selecionado oferece um desconto de 5%')
    desconto = valor*(5/100)
    valorfinal = valor-desconto
    print(
        f'O valor da compra inicial de R${valor} foi descontado para R${valorfinal:.2f}')
elif pagamento == 3:
    parcela = valor/2
    print(
        f'O método de pagamento não oferece nenhum juros ou desconto. Valor final de R${valor:.2f} em 2x de R${parcela:.2f}')
elif pagamento == 4:
    qntparcelas = int(input('Em quantas parcelas a compra será parcelada: '))
    print('O método de pagamento selecionado oferece um juros de 20%')
    juros = valor*(20/100)
    valorfinal = valor+juros
    parcela = valorfinal/qntparcelas
    print(
        f'O valor inicial de R${valor} foi acrescido em 20%, passando a ser R${valorfinal:.2f} em {qntparcelas}x de R${parcela:.2f}')
else:
    print(f'{'Saindo do programa':=^40}')
