usuario = input('Digite seu usuario: ')
qtd_caracteres = len(usuario)

if qtd_caracteres > 6:
    print(usuario, qtd_caracteres, type(qtd_caracteres))
    print(usuario.__len__())
