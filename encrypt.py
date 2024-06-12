def encrypt(public_key, message):
    message = list(map(ord, message))
    n, e = public_key[0], public_key[1] 
    def encrypt_character(character):
        return str(((character**e)%n)%n)
    return ' '.join(list(map(encrypt_character, message)))
