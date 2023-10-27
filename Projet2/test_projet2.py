import unittest
from password_generator import PasswordGenerator
from password_tester import PasswordTester
from passphrase_generator import PassphraseGenerator

class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password(self):
        generator = PasswordGenerator()
        password, entropy, strength = generator.generate_password(4, 4, 4, 4)

        self.assertEqual(len(password), 16)  # Vérifie que la longueur du mot de passe est correcte
        self.assertTrue(entropy >= 0)  # Vérifie que l'entropie est positive
        self.assertIn(strength, ["Faible", "Moyenne", "Forte"])  # Vérifie que la force est l'une des valeurs attendues

class TestPasswordTester(unittest.TestCase):
    def test_check_strength(self):
        tester = PasswordTester()
        strength = tester.check_strength("Abc123!@")
        self.assertEqual(strength, "Forte")  # Vérifie que le mot de passe est classé comme fort

    def test_check_strength_weak_password(self):
        tester = PasswordTester()
        strength = tester.check_strength("abc123")
        self.assertEqual(strength, "Faible")  # Vérifie que le mot de passe est classé comme faible

class TestPassphraseGenerator(unittest.TestCase):
    def test_generate_passphrase(self):
        eff_word_list = ["word1", "word2", "word3", "word4", "word5"]
        passphrase_generator = PassphraseGenerator(eff_word_list)
        passphrase = passphrase_generator.generate_passphrase(4)

        self.assertEqual(len(passphrase.split()), 4)  # Vérifie que le nombre de mots dans la passphrase est correct
        self.assertTrue(all(word in eff_word_list for word in passphrase.split()))  # Vérifie que les mots de la passphrase sont dans la liste de mots EFF

if __name__ == '__main__':
    unittest.main()






