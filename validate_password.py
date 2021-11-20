"""
validates a password if the following conitions are met:

          *At least 1 letter between [a-z] and 1 letter between [A-Z].
          *At least 1 number between [0-9].
          *At least 1 special character [!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~].
          *Minimum length 6 characters.
          *Maximum length 16 characters.

"""

def has_special_char(password):
    special_chars = "[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]"
    for char in special_chars:
        if char in password:
            return True
    return False


def validate(password):

    conditions = [
        password != password.upper(), # Not all letter are uppercase, atleast 1 lowercase
        password != password.lower(), # Not all letter are lowercase, atleast 1 uppercase
        has_special_char(password),   # Special character
        len(password) >= 6,           # Minimum length 6 characters
        len(password) <= 16           # Maximum length 16 characters
    ]

    return all(conditions)

if __name__ == "__main__":
    print(validate("Abc12!3"))
    print(validate("Abc12"))