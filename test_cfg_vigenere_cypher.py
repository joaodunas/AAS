import pytest
from vigenere_cipher import encrypt_message, decrypt_message

def test_P1():
    assert encrypt_message("RandomKey", "") == ""

def test_P2_1():
    assert encrypt_message("RandomKey", "*") == "*"

def test_P2_2():
    assert encrypt_message("RandomKey", "1234567890") == "1234567890"
    
def test_P2_3():
    assert encrypt_message("RandomKey", "124353465* \"?*Ç!^^~~") == "124353465* \"?*Ç!^^~~"
    
def test_P3_1():
    assert encrypt_message("RandomKey", "A") == "R"
    
def test_P3_2():
    assert encrypt_message("RandomKey", "AAAAAAAAA") == "RANDOMKEY"
    
def test_P3_3():
    assert encrypt_message("RandomKey", "LAJNSDOUASNJLDNASUDBNBUEIQNLAJSNDKAS") == "CAWQGPYYYJNWORZKWSUBAEIQSULCAWVBPUEQ"
    
def test_P4_1():
    assert decrypt_message("RandomKey", "r") == "a"
    
def test_P4_2():
    assert decrypt_message("RandomKey", "zzzzzzzzz") == "izmwlnpvb"
    
def test_P4_3():
    assert decrypt_message("RandomKey", "rdaskndnqouwndalsdn") == "adnpwbtjsxujkpobofw"
    
def test_P5_1():
    assert encrypt_message("RandomKey", "A*") == "R*"
    
def test_P5_2():
    assert encrypt_message("RandomKey", "A112LKDASMD") == "R112LXGOEWH"
    
def test_P5_3():
    assert encrypt_message("RandomKey", "A?#$%&/(AKSNDA*`ª^ª  ASD AB A134)") == "R?#$%&/(AXVBPK*`ª^ª  EQU AO D134)"

if __name__ == "__main__":
    pytest.main()