from cryptography.fernet import Fernet

# Generate and save a key
# key = Fernet.generate_key()
# with open("secret.key", "wb") as key_file:
#     key_file.write(key)

# Load the key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

def encrypt_data(data):
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Example of sending encrypted data
data = '{"timestamp": "2024-11-19 12:00:00", "heart_rate": 80, "temperature": 36.7}'
encrypted_data = encrypt_data(data)
print("Encrypted data:", encrypted_data)
