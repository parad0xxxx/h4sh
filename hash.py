#// Made by parad0x

import hashlib
import os

#// Variables
list_dir = os.listdir()
hash_lib = "MD5, SHA-1, SHA-256, SHA-384, SHA-512"
hash_dictionary = ''

#// List available hash methods
print("Available hash types: \n",hash_lib)

#// New line
print('')

#// Print available files in current directory
print("Available files to hash: \n",list_dir)

#// New line
print('')

#// Input
select = input("Enter the filename >> ")

#// New line
print('')

#// MD5 (M1)
m1=hashlib.md5()
m1.update(select.encode('utf-8'))
print("your MD5 hash is: ",m1.hexdigest())

#// SHA-1 (M2)
m2=hashlib.sha1()
m2.update(select.encode('utf-8'))
print("your SHA-1 hash is: ",m2.hexdigest())

#// SHA-256 (M3)
m3=hashlib.sha256()
m3.update(select.encode('utf-8'))
print("your SHA-256 hash is: ",m3.hexdigest())

#// SHA-384 (M4)
m4=hashlib.sha384()
m4.update(select.encode('utf-8'))
print("your SHA-384 hash is: ",m4.hexdigest())

#// SHA-512 (M5)
m5=hashlib.sha512()
m5.update(select.encode('utf-8'))
print("your SHA-512 hash is: ",m5.hexdigest())

