from keys import *
from decrypt import decrypt

private_key = list(map(int, input('key').split(' ')))
encoded_message = list(map(int, input().split(' ')))
ascii_message = decrypt(private_key, encoded_message)
message = list(map(chr, ascii_message))
print(''.join(message))
