def decrypt(private_key, message):
    n, d = private_key[0], private_key[1] 
    def decrypt_character(character):
        return ((character**d)%n)%n
    decrypted_message = list(map(decrypt_character, message))
    decrypted_message = list(map(chr, decrypted_message))
    return ''.join(decrypted_message)
