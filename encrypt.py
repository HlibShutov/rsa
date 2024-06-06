def encrypt(public_key, message):
    n, e = public_key[0], public_key[1] 
    def encrypt_character(character):
        return ((character**e)%n)%n
    return list(map(encrypt_character, message))
