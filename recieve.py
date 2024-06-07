from keys import *
from decrypt import decrypt

private_key = list(map(int, input('key').split(' ')))
encoded_message = list(map(int, input().split(' ')))
message = decrypt(private_key, encoded_message)
print(message)
