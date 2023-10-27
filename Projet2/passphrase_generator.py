import random

class PassphraseGenerator:
    def __init__(self, eff_word_list):
        self.eff_word_list = eff_word_list

    def generate_passphrase(self, num_words):
        passphrase = [random.choice(self.eff_word_list) for _ in range(num_words)]
        return ' '.join(passphrase)
