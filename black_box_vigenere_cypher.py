import unittest
from vigenere_cipher import encrypt_message, decrypt_message
    
class BlackBoxTestVigenereCipher(unittest.TestCase):  
    def black_box_test(self):
        self.assertEqual(1, 1)
    
    #Message containing only letters----------------------------------------------#
    
    #--Key containing only letters and has the same length as message-------------#
    
    #----Encrypt Mode-------------------------------------------------------------#
    def test_1(self):
        self.assertEqual(encrypt_message("def", "abc"), "dfh")

    #----Decrypt Mode-------------------------------------------------------------#
    def test_2(self):
        self.assertEqual(decrypt_message("def", "abc"), "xxx")
    
    #--Key containing only letters and longer than message------------------------#
    
    #----Encrypt Mode-------------------------------------------------------------#
    def test_3(self):
        self.assertEqual(encrypt_message("defghi", "abc"), "dfh")

    #----Decrypt Mode-------------------------------------------------------------#
    def test_4(self):
        self.assertEqual(decrypt_message("defghi", "abc"), "xxx")
    
    #--Key containing only letters and shorter than message-----------------------#
    
    #----Encrypt Mode-------------------------------------------------------------#
    def test_5(self):
        self.assertEqual(encrypt_message("de", "abc"), "dff")

    #----Decrypt Mode-------------------------------------------------------------#
    def test_6(self):
        self.assertEqual(decrypt_message("de", "abc"), "xxz")
    
    
    #Message containing any characters--------------------------------------------#
    
    #--Key containing only letters and has the same length as message-------------#
    
    #----Encrypt Mode-------------------------------------------------------------#
    def test_7(self):
        self.assertEqual(encrypt_message("defghi", "a1b#*c"), "d1f#*h")

    #----Decrypt Mode-------------------------------------------------------------#
    def test_8(self):
        self.assertEqual(decrypt_message("defghi", "a1b#*c"), "x1x#*x")
    
    #--Key containing only letters and longer than message------------------------#
    
    #----Encrypt Mode-------------------------------------------------------------#
    def test_9(self):
        self.assertEqual(encrypt_message("defghijkl", "a1b#*c"), "d1f#*h")

    #----Decrypt Mode-------------------------------------------------------------#
    def test_10(self):
        self.assertEqual(decrypt_message("defghijkl", "a1b#*c"), "x1x#*x")
    
    #--Key containing only letters and shorter than message-----------------------#
    
    #----Encrypt Mode-------------------------------------------------------------#
    def test_11(self):
        self.assertEqual(encrypt_message("def", "a1b#*c"), "d1f#*h")

    #----Decrypt Mode-------------------------------------------------------------#
    def test_12(self):
        self.assertEqual(decrypt_message("def", "a1b#*c"), "x1x#*x")


    #Message containing only non letters------------------------------------------#
    
    #--Key containing only letters and has the same length as message-------------#

    #----Encrypt Mode-------------------------------------------------------------#
    def test_13(self):
        self.assertEqual(encrypt_message("defghijklm", "1+2-3*4%#0"), "1+2-3*4%#0")

    #----Decrypt Mode-------------------------------------------------------------#
    def test_14(self):
        self.assertEqual(decrypt_message("defghijklm", "1+2-3*4%#0"), "1+2-3*4%#0")
    
    #--Key containing only letters and longer than message------------------------#
    
    #----Encrypt Mode-------------------------------------------------------------#
    def test_15(self):
        self.assertEqual(encrypt_message("defghijklmn", "1+2-3*4%#0"), "1+2-3*4%#0")

    #----Decrypt Mode-------------------------------------------------------------#
    def test_16(self):
        self.assertEqual(decrypt_message("defghijklmn", "1+2-3*4%#0"), "1+2-3*4%#0")
    
    #--Key containing only letters and shorter than message-----------------------#
    
    #----Encrypt Mode-------------------------------------------------------------#
    def test_17(self):
        self.assertEqual(encrypt_message("def", "1+2-3*4%#0"), "1+2-3*4%#0")

    #----Decrypt Mode-------------------------------------------------------------#
    def test_18(self):
        self.assertEqual(decrypt_message("def", "1+2-3*4%#0"), "1+2-3*4%#0")
    
    
if __name__ == "__main__":
    unittest.main()