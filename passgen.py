import random
import string

def generate_password(length: int = 12): #modify for your desired length
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(alphabet, length))
    simplepassword = "".join(random.sample(string.ascii_letters + string.digits, length))
    both = "Simple Password: " + simplepassword + "\nPassword: " + password
    return both


for i in range(10):
    genpassword = generate_password()
    print(genpassword)


