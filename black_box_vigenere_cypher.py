import pytest
from vigenere_cipher import encrypt_message, decrypt_message

#----------------------Test Cases----------------------#
#------------Message containing only letters-----------#

def test_1():
    assert encrypt_message("def", "abc") == "dfh"

def test_2():
    assert decrypt_message("def", "abc") == "xxx"
    
def test_3():
    assert encrypt_message("defghi", "abc") == "dfh"

def test_4():
    assert decrypt_message("defghi", "abc") == "xxx"
    
def test_5():
    assert encrypt_message("de", "abc") == "dff"

def test_6():
    assert decrypt_message("de", "abc") == "xxz"
    
    
#-----------Message containing any characters----------#

def test_7():
    assert encrypt_message("defghi", "a1b#*c") == "d1f#*h"

def test_8():
    assert decrypt_message("defghi", "a1b#*c") == "x1x#*x"
    
def test_9():
    assert encrypt_message("defghijkl", "a1b#*c") == "d1f#*h"

def test_10():
    assert decrypt_message("defghijkl", "a1b#*c") == "x1x#*x"
    
def test_11():
    assert encrypt_message("def", "a1b#*c") == "d1f#*h"

def test_12():
    assert decrypt_message("def", "a1b#*c") == "x1x#*x"


#----------Message containing only non letters---------#

def test_7():
    assert encrypt_message("defghijklm", "1+2-3*4%#0") == "1+2-3*4%#"

def test_8():
    assert decrypt_message("defghijklm", "1+2-3*4%#0") == "1+2-3*4%#"
    
def test_9():
    assert encrypt_message("defghijklmn", "1+2-3*4%#0") == "1+2-3*4%#"

def test_10():
    assert decrypt_message("defghijklmn", "1+2-3*4%#0") == "1+2-3*4%#"
    
def test_11():
    assert encrypt_message("def", "1+2-3*4%#0") == "1+2-3*4%#"

def test_12():
    assert decrypt_message("def", "1+2-3*4%#0") == "1+2-3*4%#"
    

if __name__ == "__main__":
    pytest.main()