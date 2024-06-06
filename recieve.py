from generate_keys import keys_generator

public_key, private_key = keys_generator()
message = list(input())
ascii_message = list(map(ord, message))

