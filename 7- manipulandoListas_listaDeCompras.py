lista = []

opc = -1

while opc != 0:
  print('MENU '
  '\n[1] Adicionar produto: '
  '\n[2] Exibir lista'
  '\n[3] Remover ultimo item'
  '\n[4] Remover: '
  '\n[0] Encerrar') 

  opc = int(input('Digite sua escolha: '))

  if opc == 1:
    produto = input('Digite o nome do produto: ')
    lista.append(produto)
  elif opc == 2:
    print(lista, '\n')
  elif opc == 3:
    lista.pop()
  elif opc == 4:
    produto = input('Digite o produto que deseja remover:  ')
    lista.remove(produto)
  else:
    print('Essa opção é inválida')
  
