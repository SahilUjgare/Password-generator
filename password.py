import string
import random

class PasswordGenerator:
    def __init__(self, length=12):
      
        """
        Initialize PasswordGenerator with desired password length.
        Default length is 12 characters.
        """

        self.length = length
        self.characters = string.ascii_letters + string.digits + string.punctuation

    def generate_password(self):
        """Generates a strong password of given length.
           Ensures that password contains at least:
           - One lowercase letter
           - One uppercase letter
           - One digit
           - One special character
           """

        if self.length < 4:
            raise ValueError("Password length must be at least 4 characters.")

        # Guarantee required characters
        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]

        # Fill remaining characters randomly
        password += random.choices(self.characters, k=self.length - 4)

        # Shuffle to avoid predictable pattern
        random.shuffle(password)

        return ''.join(password)


if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length: "))
        generator = PasswordGenerator(length)
        print("Generated Strong Password:", generator.generate_password())
    except ValueError as e:
        print("Error:", e)


