def decrypt(private_key, message):
    n, d = private_key[0], private_key[1] 
    def decrypt_character(character):
        return ((character**d)%n)%n
    return list(map(decrypt_character, message))
