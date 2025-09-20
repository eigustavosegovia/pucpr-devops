from src.main import *

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_subtrair():
    assert subtrair(10, 4) == 6
    assert subtrair(0, 5) == -5

def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(-2, 3) == -6

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(4, 2) == 2

def test_fatorial():
    assert fatorial(5) == 120
    assert fatorial(0) == 1
