num_1 = 10
num_2 = 3
divisao = num_1 / num_2
teste = 'nome teste'
teste_formatado = '{:@>20}'.format(teste)
teste2 = teste.ljust(20, '#')

print( '{:.2f}'.format(divisao) )
print(f'{divisao:.2f}')

print(f'{num_1:0>10}')
print(f'{num_2:0^10}')
print(f'{num_2:0<10}')

print(f'{teste:#^50}')
print(teste_formatado)
print(teste2)

print(teste.lower())
print(teste.upper())
print(teste.title()) # Primeiras letras maiusculas
