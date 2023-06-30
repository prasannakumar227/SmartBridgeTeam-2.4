# Basic Caeser Cipher implementation using Python programming language
# By KAMALESH, 20MIS0342, VIT-VELLORE, #CyberSecurity&EthicalHacking

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_text = encrypted_text + encrypted_char
        else:
            encrypted_text = encrypted_text + char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

# Code from 20MIS0342
plaintext = input("Enter plaintext: ")
shift = 3

encrypted = encrypt(plaintext, shift)
print("\nEncrypted text:", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted text:",decrypted)