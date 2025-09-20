from src.main import *

def test_aluno():
    avaliar_aluno_teste = avaliar_aluno()
    assert avaliar_aluno_teste["Situação"] == "Aprovado"
