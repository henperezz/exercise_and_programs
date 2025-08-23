ano=int(input('Digite um ano qualquer: '))

bissexto=ano%4

if bissexto==0 and ano%100!=0 or ano%400==0:
    print(f'O ano de {ano} é bissexto!')
else:
    print(f'O ano de {ano} não é bissexto!')