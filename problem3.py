import datetime
import hashlib
import pickle 


def double_sha256(data): 
     """Double hashes input data. Output is 32 bytes"""
     hash1 = hashlib.sha256(data).digest()
     return hashlib.sha256(hash1).digest()


if __name__ == '__main__':

     # test function to ensure hash function is working correctly 
     # https://docs.python.org/3/library/hashlib.html
     # byte_str = 'Nobody inspects the spammish repetition'.encode()
     # print(hashlib.sha256(byte_str).hexdigest())

     # current time as Unix Epoch format 
     now_epoch_time = datetime.datetime.now().timestamp()

     # set 1 
     set1 = {
          '0000000036dc2ce23cdd934eff4bae120155de8b8712de8489c8870b06e334ff',
          'c0ba5ba1c5ba02fb02c4ea93ec16cae7ea1994b5b3f9ef0e293b841081eb3003',
          now_epoch_time,
          1.00000,
          5251252
     }

     # set 2 
     set2 = {
          '00000000d84724559f1691d916b2ed63a44884d495d155197647ce7667116b16',
          '69a14e6b050d10d6621faee3dac6682809feb0ffa76320b33c5c09f1059f06c7',
          now_epoch_time,
          1.00000,
          124867778
     }

     # serialize set objects into byte streams
     byte_set1 = pickle.dumps(set1, protocol=pickle.DEFAULT_PROTOCOL)
     byte_set2 = pickle.dumps(set2, protocol=pickle.DEFAULT_PROTOCOL)

     # double hash left, right sets 
     sha_left = double_sha256(byte_set1)
     # print sha_left
     print(sha_left)
     sha_right = double_sha256(byte_set2)
     # print sha_right
     print(sha_right)

     # per conversation with Allen we concatenate as hex strings 
     root_hex = sha_left.hex() + sha_right.hex()

     # encode concatenated hex strings as bytes, hash 
     root = hashlib.sha256(root_hex.encode('utf-8')).digest()

     # print root as hex 
     print(root.hex())

