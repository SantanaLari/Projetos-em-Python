lanche = ('hamburguer', 'batata frita', 'pastel', 'coxinha')

#exibir lanche na posição 2
print(lanche[2])

#organiza os lanches
print(sorted(lanche))

#exibe posição e lanche com enumerate
for posicao, comida in enumerate(lanche):
  print(f'Posição: {posicao}- {comida}')

#exibe apenas lanche
for c in lanche:
  print (c)
