def avaliar_aluno():
    aluno = {}
    aluno["Nome"] = input("Digite o nome do aluno: ")
    aluno["Média"] = float(input("Digite a média do aluno: "))

    if aluno["Média"] < 5:
        aluno["Situação"] = "Reprovado"
    elif aluno["Média"] < 7:
        aluno["Situação"] = "Recuperação"
    else:
        aluno["Situação"] = "Aprovado"
        
    return aluno


# Exemplo de uso
print(avaliar_aluno())
