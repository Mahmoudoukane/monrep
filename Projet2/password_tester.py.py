import string

class PasswordTester:
    def check_strength(self, password):
        # Vérifier la force du mot de passe en fonction de critères spécifiques
        if len(password) < 8:
            return "Faible"  # Mot de passe trop court
        elif any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password):
            return "Forte"  # Contient des lettres minuscules, majuscules, chiffres et caractères spéciaux
        else:
            return "Moyenne"  # Autres cas

    def additional_criteria(self, password):
        # Ajoutez ici des critères de force supplémentaires si nécessaire
        pass



