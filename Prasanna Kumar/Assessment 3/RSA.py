import random
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

p = random.randint(2**31, 2**32)
while not is_prime(p):
    p = random.randint(2**31, 2**32)

q = random.randint(2**31, 2**32)
while not is_prime(q) or q == p:
    q = random.randint(2**31, 2**32)

n = p * q
phi = (p - 1) * (q - 1)

e = random.randint(2, phi)
while math.gcd(e, phi) != 1:
    e = random.randint(2, phi)

d = pow(e, -1, phi)

message = input("Enter the plaintext: ")
plaintext = message.encode('utf-8')

ciphertext = pow(int.from_bytes(plaintext, 'big'), e, n)
decrypted_plaintext = pow(ciphertext, d, n)

try:
    decrypted_message = decrypted_plaintext.to_bytes((decrypted_plaintext.bit_length() + 7) // 8, 'big').decode('utf-8')
except UnicodeDecodeError:
    decrypted_message = decrypted_plaintext.to_bytes((decrypted_plaintext.bit_length() + 7) // 8, 'big').decode('latin-1')

print("Plaintext (bytes):", " ".join([str(byte) for byte in plaintext]))
print("Public keys (e, n):", e, n)
print("Ciphertext:", ciphertext)
print("Decrypted Message:", decrypted_message)
