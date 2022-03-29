import random
import string

characters = list(string.ascii_letters + string.digits + string.punctuation)

def genPass():
    lenght = int(input("Pass lenght: "))
    random.shuffle(characters)

    password = []
    for i in range(lenght):
        password.append(random.choice(characters))

    random.shuffle(password)
    print("".join(password))
