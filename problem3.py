import datetime
import hashlib
import pickle 

# questions
# are functions with docstrings required?
# do we need to git repo or should we just submit direct to svn?
# what is a response file?

# a) serialize the data into a bytestream for each set of data
# sets do not maintain order - is that okay?
# python pickle to serialize data into bytestream 

# b) appears from the example we are meant to:
     # double hash requires byte encoding, so it must be bytes -> hash1 -> hashedbytes1 -> hash2 -> hashbytes2
     # the lab says 'Note you are concatenating two 32-byte hex strings of numbers' 
     # implies hex + hex = concatenated hex, then encoded to bytes, then hashed 

# c) do you want use to print as hex or bytes?

# d) question on lab 4

now_epoch_time = datetime.datetime.now().timestamp()
print(now_epoch_time)

set1 = {
     '0000000036dc2ce23cdd934eff4bae120155de8b8712de8489c8870b06e334ff',
     'c0ba5ba1c5ba02fb02c4ea93ec16cae7ea1994b5b3f9ef0e293b841081eb3003',
     now_epoch_time,
     1.00000,
     5251252
}

set2 = {
     '00000000d84724559f1691d916b2ed63a44884d495d155197647ce7667116b16',
     '69a14e6b050d10d6621faee3dac6682809feb0ffa76320b33c5c09f1059f06c7',
     now_epoch_time,
     1.00000,
     124867778
}

# convert set to string
# note that sets dont have order - if order must be preserved than this would be an ordered set
# str_set1 = str(set1)
# str_set2 = str(set2)
# byte_str_set1 = str_set1.encode('utf-8')
# byte_str_set2 = str_set2.encode('utf-8')

# serialize into byte stream
byte_set1 = pickle.dumps(set1, protocol=pickle.DEFAULT_PROTOCOL)
byte_set2 = pickle.dumps(set2, protocol=pickle.DEFAULT_PROTOCOL)

# https://docs.python.org/3/library/hashlib.html
byte_str = 'Nobody inspects the spammish repetition'.encode()
print(hashlib.sha256(byte_str).hexdigest())

def double_sha256(data): 
     """Double hashes input data. Output is 32 bytes"""
     hash1 = hashlib.sha256(data).digest()
     return hashlib.sha256(hash1).digest()

# def double_sha256_hex(data): 
#      """Double hashes input data. Output is 32 bytes"""
#      hash1 = hashlib.sha256(data).hexdigest()
#      return hashlib.sha256(hash1).hexdigest()
# sha_left_hex = double_sha256_hex(byte_str_set1)

sha_left = double_sha256(byte_set1)
sha_right = double_sha256(byte_set2)
root_hex = sha_left.hex() + sha_right.hex()
root = hashlib.sha256(root_hex.encode('utf-8')).digest()
print(root)
# root = hashlib.sha256(sha_left + sha_right).digest()
# print(root)
