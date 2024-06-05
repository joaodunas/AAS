import unittest
from vigenere_cipher import encrypt_message, decrypt_message

class TestVigenereCipher(unittest.TestCase):
    def black_box_test(self):
        self.assertEqualEqual(1, 1)
    
    #Empty message---------------------------------------------------------------------------------#
    def test_P1(self):
        self.assertEqual(encrypt_message("RandomKey", ""), "")

    #Message with just one character outside the alphabet------------------------------------------#
    def test_P2_1(self):
        self.assertEqual(encrypt_message("RandomKey", "*"), "*")

    #Message with various characters outside the alphabet------------------------------------------#
    def test_P2_2(self):
        self.assertEqual(encrypt_message("RandomKey", "1234567890"), "1234567890")
    
    #Message with even more characters outside the alphabet----------------------------------------#
    def test_P2_3(self):
        self.assertEqual(encrypt_message("RandomKey", "124353465* \"?*Ç!^^~~"), "124353465* \"?*Ç!^^~~")
    
    #Message with only one character inside the alphabet in uppercase in encrypt mode--------------#
    def test_P3_1(self):
        self.assertEqual(encrypt_message("RandomKey", "A"), "R")
    
    #Message with various characters inside the alphabet in uppercase in encrypt mode--------------#
    def test_P3_2(self):
        self.assertEqual(encrypt_message("RandomKey", "AAAAAAAAA"), "RANDOMKEY")
    
    #Message with even more characters inside the alphabet in encrypt mode-------------------------#
    def test_P3_3(self):
        self.assertEqual(encrypt_message("RandomKey", "LAJNSDOUASNJLDNASUDBNBUEIQNLAJSNDKAS"), "CAWQGPYYYJNWORZKWSUBAEIQSULCAWVBPUEQ")
    
    #Message with only one character inside the alphabet in lowercase in decrypt mode--------------#
    def test_P4_1(self):
        self.assertEqual(decrypt_message("RandomKey", "r"), "a")
    
    #Message with various characters inside the alphabet in lowercase in decrypt mode--------------#
    def test_P4_2(self):
        self.assertEqual(decrypt_message("RandomKey", "zzzzzzzzz"), "izmwlnpvb")
    
    #Message with even more characters inside the alphabet in lowercase in decrypt mode------------#
    def test_P4_3(self):
        self.assertEqual(decrypt_message("RandomKey", "rdaskndnqouwndalsdn"), "adnpwbtjsxujkpobofw")
    
    #Message with 2 characters, combining one from alphabet with one outside-----------------------#
    def test_P5_1(self):
        self.assertEqual(encrypt_message("RandomKey", "A*"), "R*")
    
    #Message combining some characters from alphabet with some outside-----------------------------#
    def test_P5_2(self):
        self.assertEqual(encrypt_message("RandomKey", "A112LKDASMD"), "R112LXGOEWH")
    
    #Message combining even more characters from alphabet with some outside------------------------#
    def test_P5_3(self):
        self.assertEqual(encrypt_message("RandomKey", "A?#$%&/(AKSNDA*`ª^ª  ASD AB A134)"), "R?#$%&/(AXVBPK*`ª^ª  EQU AO D134)")
    
if __name__ == "__main__":
    unittest.main()