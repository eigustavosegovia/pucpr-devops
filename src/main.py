def avaliar_aluno(nome, media):
    aluno = {}
    aluno["Nome"] = nome
    aluno["Média"] = media
    if aluno["Média"] < 5:
        aluno["Situação"] = "Reprovado"
    elif aluno["Média"] < 7:
        aluno["Situação"] = "Recuperação"
    else:
        aluno["Situação"] = "Aprovado"
        
    return aluno


# Exemplo de uso
print(avaliar_aluno())
