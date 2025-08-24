# Atividde da disciplina
aluno = {}
nome = str(input("Digite o nome do aluno: "))
aluno["Nome"] = nome
media = float(input("Digite a média do aluno: "))
aluno["Média"] = media
if media < 5:
    aluno["Situação"] = "Reprovado"
elif media < 7:
    aluno["Situação"] = "Recuperação"
else:
    aluno["Situação"] = "Aprovado"
print("-=" * 30)
print(f'''Aluno: {aluno["Nome"]}
Média: {aluno["Média"]}
Situação: {aluno["Situação"]}''')