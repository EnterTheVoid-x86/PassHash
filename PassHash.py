# PassHash password generator
import random
import string
import sys


try:
    if sys.argv[1] == "--debug":
        print("Debug mode")
        debug = True
    else:
        debug = False
except IndexError:
    debug = False
    pass

available = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_password():
    length = int(input("Password length: "))
    if length > 128:
        print("Be reasonable! Use a number between 8 and 128.")
        sys.exit(1)
    if length < 8:
        print("Your password length is too short! That won't keep you safe.")
        sys.exit(1)
    if debug == True:
        print("Shuffling available characters")
        print("Creating password")
        print("Shuffling password characters")
        print("Printing password...")
    random.shuffle(available)
    password = []
    for i in range(length):
        password += [random.choice(available)]

        
    random.shuffle(password)

    print("Generated password:")
    print("".join(password))

generate_password()
    