from encrypt import encrypt 

public_key = list(map(int, input('key').split(' ')))
message = list(input())
encrypted_message = encrypt(public_key, message)
print(encrypted_message)
