import unittest
from main import encrypt, decrypt


class TestCaesarCipher(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt("hello", 3), "khoor")
        self.assertEqual(encrypt("world", 1), "xpsme")
        self.assertEqual(encrypt("python", 13), "clguba")

    def test_decrypt(self):
        self.assertEqual(decrypt("khoor", 3), "hello")
        self.assertEqual(decrypt("xpsme", 1), "world")
        self.assertEqual(decrypt("clguba", 13), "python")

    def test_encrypt_decrypt(self):
        plaintext = "the quick brown fox jumps over the lazy dog"
        shift = 5
        self.assertEqual(decrypt(encrypt(plaintext, shift), shift), plaintext)


if __name__ == "__main__":
    unittest.main()
