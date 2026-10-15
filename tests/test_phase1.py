import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine import phase1_encrypt, phase1_decrypt

key = {"shift": 7}

message = "Hello CipherForge!"
encrypted = phase1_encrypt(message, key)
print(f"Encrypted: {encrypted}")

decrypted = phase1_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")

print(f"Match: {decrypted == message}")

def encrypt(text, key):
      result = phase1_encrypt(text, key)
      
      return result
      
def decrypt(text, key):
      result = text
      
      result = phase1_decrypt(result, key)
      
      return result

for shift in (1, 13, 50):
      k = {"shift": shift}
      sample = "Attack at dawn!"
      enc = phase1_encrypt(sample, k)
      dec = phase1_decrypt(enc, k)
      print(f"shift={shift}: enc='{enc}' dec_match={dec == sample}")