nomeAluno = input('Digite o nome do aluno: ').title()
idadeAluno = int(input('Digite a idade do aluno: '))
prova1 = float(input('Digite a nota da primeira prova: '))
prova2 = float(input('Digite a nota da segunda prova: '))

media = (prova1 + prova2) / 2

print('Nome: ', nomeAluno)

if idadeAluno >= 18:
    if media >= 6:
        print('Aprovado')
    else:
        print('Reprovado')
else:
    print('Reprovado')

