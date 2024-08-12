from encrypt import *
from decrypt import *

print("Enter a string : ")
s=input()

s_encrypted=encrypt(s)
s_decrypted=decrypt(s_encrypted)

print("String after encryption : ",s_encrypted)

print("String after decryption : ",s_decrypted)