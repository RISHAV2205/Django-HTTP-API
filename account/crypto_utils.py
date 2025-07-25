from cryptography.fernet import Fernet
from django.conf import settings

fernet = Fernet(settings.ENCRYPT_KEY.encode())

def encrypt_password(password: str) -> str:
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(encrypted: str) -> str:
    return fernet.decrypt(encrypted.encode()).decode()
