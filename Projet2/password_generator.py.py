import random
import string
import math

class PasswordGenerator:
    def generate_password(self, num_lower, num_upper, num_digits, num_special):
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special = string.punctuation

        characters = []

        for _ in range(num_lower):
            characters.append(random.choice(lowercase))
        for _ in range(num_upper):
            characters.append(random.choice(uppercase))
        for _ in range(num_digits):
            characters.append(random.choice(digits))
        for _ in range(num_special):
            characters.append(random.choice(special))

        random.shuffle(characters)
        password = ''.join(characters)

        # Calcul de l'entropie
        alphabet_size = 94  # Total des caractères possibles
        password_length = len(password)
        entropy = password_length * math.log2(alphabet_size)

        # Calcul de la force du mot de passe
        strength = "Faible"
        if entropy >= 30:
            strength = "Moyenne"
        if entropy >= 60:
            strength = "Forte"

        return password, entropy, strength

    def calculate_entropy(self, password):
        alphabet_size = 94  # Total des caractères possibles
        password_length = len(password)
        entropy = password_length * math.log2(alphabet_size)
        return entropy

    def check_strength(self, password):
        entropy = self.calculate_entropy(password)
        if entropy < 30:
            return "Faible"
        elif entropy < 60:
            return "Moyenne"
        else:
            return "Forte"



