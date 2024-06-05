import unittest
from vigenere_cipher import translate_message


class TestDF_key(unittest.TestCase):
    # def test_p1(self): #(1, 2, 3, 4, 5, 9, 10, 12, 14, 2, 16) #imposible if it goes through 5 it has to enter in 11 or 13
    # mode == "encrypt"
    # ~symbol.isupper()
    # ~symbol.islower()
    # ~symbol in message
    #    self.assertEqual()
    def test_p2(self):  # (1, 2, 3, 4, 5, 9, 10, 11, 14, 2, 16)
        # mode == "encrypt"
        # symbol.isupper()
        # key_index != len(key)
        # so message has only 1 symbol and it is a upper case letter
        # key has len more than 1 so key_index != len(key)
        message = ["A"]
        key = "key"
        mode = "encrypt"
        self.assertEqual([translate_message(key, message, mode)], ["K"])

    def test_p3(self):  # (1, 2, 3, 4, 5, 9, 10, 12, 13, 14, 2, 16)
        # mode == "encrypt"
        # symbol.islower()
        # key_index != len(key)
        # so message has only 1 symbol and it is a lower case letter
        # key has len more than 1 so key_index != len(key)
        message = ["a"]
        key = "key"
        mode = "encrypt"
        self.assertEqual([translate_message(key, message, mode)], ["k"])

    # def test_p4(self): #(1, 2, 3, 4, 7, 8, 9, 10, 12, 14, 2, 16)
    # #impossible like P(1)
    #    self.assertEqual()

    def test_p5(self):  # (1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 2, 16)
        # mode == "decrypt"
        # symbol.isupper()
        # key_index != len(key)
        # so message has only 1 symbol and it is a upper case letter
        # key has len more than 1 so key_index != len(key)
        message = ["A"]
        key = "key"
        mode = "decrypt"
        self.assertEqual([translate_message(key, message, mode)], ["Q"])

    def test_p6(self):  # (1, 2, 3, 4, 7, 8, 9, 10, 12, 13, 14, 2, 16)
        # mode == "decrypt"
        # symbol.islower()
        # key_index != len(key)
        # so message has only 1 symbol and it is a lower case letter
        # key has len more than 1 so key_index != len(key)
        message = ["a"]
        key = "key"
        mode = "decrypt"
        self.assertEqual([translate_message(key, message, mode)], ["q"])

    # def test_p7(self): #(1, 2, 3, 4, 5, 9, 10, 12, 14, 15, 2, 16)
    ## impossible for the same reason as P(1)
    #   self.assertEqual()

    def test_p8(self):  # (1, 2, 3, 4, 5, 9, 10, 11, 14, 15, 2, 16)
        # mode == "encrypt"
        # symbol.isupper()
        # key_index == len(key)
        # so message has only 1 symbol and it is a upper case letter
        # key has len 1 so key_index == len(key)
        message = ["A"]
        key = "k"
        mode = "encrypt"
        self.assertEqual([translate_message(key, message, mode)], ["K"])

    def test_p9(self):  # (1, 2, 3, 4, 5, 9, 10, 12, 13, 14, 15, 2, 16)
        # mode == "encrypt"
        # symbol.islower()
        # key_index == len(key)
        # so message has only 1 symbol and it is a lower case letter
        # key has len 1 so key_index == len(key)
        message = ["a"]
        key = "k"
        mode = "encrypt"
        self.assertEqual([translate_message(key, message, mode)], ["k"])

    # def test_p10(self): #(1, 2, 3, 4, 7, 9, 10, 12, 14, 15, 2, 16)
    ##impossible for the same reason as P(1)
    #    self.assertEqual()

    def test_p11(self):  # (1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 15, 2, 16)
        # mode == "decrypt"
        # symbol.isupper()
        # key_index == len(key)
        # so message has only 1 symbol and it is a upper case letter
        # key has len 1 so key_index == len(key)
        message = ["A"]
        key = "k"
        mode = "decrypt"
        self.assertEqual([translate_message(key, message, mode)], ["Q"])

    def test_p12(self):  # (1, 2, 3, 4, 7, 8, 9, 10, 12, 13, 14, 15, 2, 16)
        # mode == "decrypt"
        # symbol.islower()
        # key_index == len(key)
        # so message has only 1 symbol and it is a lower case letter
        # key has len 1 so key_index == len(key)
        message = ["a"]
        key = "k"
        mode = "decrypt"
        self.assertEqual([translate_message(key, message, mode)], ["q"])


if __name__ == "__main__":
    unittest.main()
