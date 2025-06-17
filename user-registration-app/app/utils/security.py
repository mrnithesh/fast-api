import hashlib

def hashPassword(password:str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()