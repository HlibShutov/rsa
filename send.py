from encrypt import encrypt 

public_key = list(map(int, input('key').split(' ')))
message = list(input())
ascii_message = list(map(ord, message))
encrypted_message = encrypt(public_key, ascii_message)
print(encrypted_message)
