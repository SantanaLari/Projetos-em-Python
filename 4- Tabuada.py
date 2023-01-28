numero = int(input('Digite a tabuada que você deseja visualizar: '))

for c in range(0, 11):
    res = c * numero
    print(numero, ' x ', c, ' = ', res)
