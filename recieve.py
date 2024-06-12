from keys import *
from decrypt import decrypt

def recieve(private_key, message):
    return decrypt(private_key, message)
