from py2cfg import CFGBuilder

cfg = CFGBuilder().build_from_file("vigenere_cipher", "./vigenere_cipher.py")

cfg.build_visual("vigenere_cipher_cfg", "pdf")
