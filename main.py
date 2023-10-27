from password_generator import PasswordGenerator
from password_tester import PasswordTester
from passphrase_generator import PassphraseGenerator

def main():
    generator = PasswordGenerator()
    tester = PasswordTester()

    eff_word_list = None
    with open(r'C:\Users\kanem\monrep\eff_large_wordlist.txt', 'r') as file: 
        eff_word_list = [line.strip() for line in file]

    passphrase_generator = PassphraseGenerator(eff_word_list)  # Initialisez le générateur basé sur les mots de l'EFF

    while True:
        print("Options:")
        print("1. Générer un mot de passe personnalisé")
        print("2. Générer un mot de passe aléatoire")
        print("3. Générer une passphrase aléatoire (EFF)")

        try:
            option = int(input("Sélectionnez une option (1, 2 ou 3) : ")) 

            if option == 1:
                num_lower = int(input("Nombre de lettres minuscules : "))
                num_upper = int(input("Nombre de lettres majuscules : "))
                num_digits = int(input("Nombre de chiffres : "))
                num_special = int(input("Nombre de caractères spéciaux : "))

                # Générez votre mot de passe personnalisé ici
                custom_password, custom_entropy, custom_strength = generator.generate_password(num_lower, num_upper, num_digits, num_special)

                # Évaluez la force du mot de passe personnalisé ici
                custom_password_strength = tester.check_strength(custom_password)

                print("Mot de passe personnalisé :", custom_password)
                print("Entropie du mot de passe personnalisé :", custom_entropy)
                print("Force du mot de passe personnalisé :", custom_password_strength)

            elif option == 2:
                # Générez votre mot de passe aléatoire ici
                random_password, random_entropy, random_strength = generator.generate_password(4, 4, 4, 4)

                print("Mot de passe aléatoire :", random_password)
                print("Entropie du mot de passe aléatoire :", random_entropy)
                print("Force du mot de passe aléatoire :", random_strength)

            elif option == 3:
                num_words = int(input("Nombre de mots dans la passphrase : "))
                eff_passphrase = passphrase_generator.generate_passphrase(num_words)
                print("Passphrase générée (EFF) :", eff_passphrase)

            else:
                print("Option non valide. Veuillez sélectionner 1, 2 ou 3.")
        except ValueError:
            print("Option non valide. Veuillez sélectionner 1, 2 ou 3.")

if __name__ == "__main__":
    main()













