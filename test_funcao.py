import pytest
from teste_op import somar
from teste_op import subtrair

def test_somar():
    assert somar(2, 3) == 5

def test_subtrair():
    assert subtrair(2, 3) == -1