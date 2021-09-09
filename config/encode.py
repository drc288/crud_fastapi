from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

def encode(password):
    return f.encrypt(password)