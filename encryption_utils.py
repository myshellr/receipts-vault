from cryptography.fernet import Fernet

# Create a new encryption key
def generate_key():
    return Fernet.generate_key()

# Save the encryption key to a file
def save_key(key, filename='secret.key'):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

# Load the encryption key from a file
def load_key(filename='secret.key'):
    with open(filename, 'rb') as key_file:
        return key_file.read()

# Encrypt a note with the key
def encrypt_note(note_text, key):
    f = Fernet(key)
    return f.encrypt(note_text.encode())

# Decrypt a note with the key
def decrypt_note(encrypted_note, key):
    f = Fernet(key)
    return f.decrypt(encrypted_note).decode()

