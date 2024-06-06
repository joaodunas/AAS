import unittest
from vigenere_cipher import encrypt_message, decrypt_message
    
class BlackBoxTestVigenereCipher(unittest.TestCase):  
    def black_box_test(self):
        self.assertEqual(1, 1)
    
    #Message containing only letters----------------------------------------------#
    
    #--Key containing one more letter than message--------------------------------#
    
    #----Encrypt Mode-------------------------------------------------------------#
    def test_1(self):
        self.assertEqual(encrypt_message("defg", "abc"), "dfh")

    #----Decrypt Mode-------------------------------------------------------------#
    def test_2(self):
        self.assertEqual(decrypt_message("defg", "abc"), "xxx")
    
    #--Key containing one less letter than message--------------------------------#
    
    #----Encrypt Mode-------------------------------------------------------------#
    def test_3(self):
        self.assertEqual(encrypt_message("de", "abc"), "dff")

    #----Decrypt Mode-------------------------------------------------------------#
    def test_4(self):
        self.assertEqual(decrypt_message("de", "abc"), "xxz")
    
    
    #Message containing any characters--------------------------------------------#
    
    #--Key containing one more letter than message--------------------------------#
    
    #----Encrypt Mode-------------------------------------------------------------#
    def test_5(self):
        self.assertEqual(encrypt_message("defghij", "a1b#*c"), "d1f#*h")

    #----Decrypt Mode-------------------------------------------------------------#
    def test_6(self):
        self.assertEqual(decrypt_message("defghij", "a1b#*c"), "x1x#*x")
    
    #--Key containing one less letter than message--------------------------------#
    
    #----Encrypt Mode-------------------------------------------------------------#
    def test_7(self):
        self.assertEqual(encrypt_message("defgh", "a1b#*c"), "d1f#*h")

    #----Decrypt Mode-------------------------------------------------------------#
    def test_8(self):
        self.assertEqual(decrypt_message("defgh", "a1b#*c"), "x1x#*x")


    #Message containing only non letters------------------------------------------#
    
    #--Key containing one more letter than message--------------------------------#
    
    #----Encrypt Mode-------------------------------------------------------------#
    def test_9(self):
        self.assertEqual(encrypt_message("defghijklmn", "1+2-3*4%#0"), "1+2-3*4%#0")

    #----Decrypt Mode-------------------------------------------------------------#
    def test_10(self):
        self.assertEqual(decrypt_message("defghijklmn", "1+2-3*4%#0"), "1+2-3*4%#0")
    
    #--Key containing one less letter than message--------------------------------#
    
    #----Encrypt Mode-------------------------------------------------------------#
    def test_11(self):
        self.assertEqual(encrypt_message("defghijkl", "1+2-3*4%#0"), "1+2-3*4%#0")

    #----Decrypt Mode-------------------------------------------------------------#
    def test_12(self):
        self.assertEqual(decrypt_message("defghijkl", "1+2-3*4%#0"), "1+2-3*4%#0")
    
    
if __name__ == "__main__":
    unittest.main()