import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.main import *

from src.main import *

def test_aluno():
    avaliar_aluno_teste = avaliar_aluno(nome="teste", media= 9)
    assert avaliar_aluno_teste["Situação"] == "Aprovado"
