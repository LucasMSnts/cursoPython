#       [123456789] positivos
texto = "testando!"
#       [987654321] negativos

nova_string = texto[2:6]
print(nova_string)
nova_string = texto[:6]
print(nova_string)
nova_string = texto[6:]
print(nova_string)
nova_string = texto[:-2]
print(nova_string)
nova_string = texto[0::2]
print(nova_string)

for letra in texto:
    print(letra)