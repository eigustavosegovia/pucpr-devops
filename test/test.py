from src.main import *


def test_aluno():
    avaliar_aluno_teste = avaliar_aluno(nome="teste", media= 9)
    assert avaliar_aluno_teste["Situação"] == "Aprovado"
