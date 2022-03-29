from random import shuffle, choice

import string

CHARACTERS = list(string.ascii_letters + string.digits + string.punctuation)

def genPass(characters=CHARACTERS, lenght=8):
    """ Generate a password """
    shuffle(characters)

    password = []
    for _ in range(lenght):
        password.append(choice(characters))

    shuffle(password)
    return ''.join(password)
