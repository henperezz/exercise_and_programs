valorcasa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o seu salário? R$'))
qntanos = int(input('Em quantos anos vai parcelar? '))

vlrparc = valorcasa/(qntanos*12)
limiteparc = salario*(30/100)

print(f'''O banco atua com um limite de parcela de 30% de seu atual salário,
 o limite é de R${limiteparc:.2f}.''')

if vlrparc > limiteparc:
    print(f'''O valor da parcela será de R${vlrparc:.2f}, porém
 seu empréstimo foi negado por ultrapassar 30% do seu salário
total!!''')
else:
    print(f'''O valor da parcela será de R${vlrparc:.2f}, seu empréstimo
 foi aprovado!''')
