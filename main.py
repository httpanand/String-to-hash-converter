import hashlib
tohash = input('Enter a string value to convert into hash value')
hash_obj = hashlib.md5(tohash.encode())
print('----------------------------------------\n''HASH VALUE = ' , hash_obj.hexdigest(),'\n----------------------------------------')
