nome = 'Lucas'
idade = 26
altura = 1.78
peso = 80.5
ano_atual = 2022
nascimento= ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso} e seu imc é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')