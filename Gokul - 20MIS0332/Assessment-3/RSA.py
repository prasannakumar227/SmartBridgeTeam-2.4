import random


def is_prime(num):
    # Check if a number is prime
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_prime():
    # Generate a large prime number
    while True:
        num = random.randint(2 ** 10, 2 ** 11)
        if is_prime(num):
            return num


def compute_gcd(a, b):
    # Compute the greatest common divisor (GCD) of two numbers
    while b != 0:
        a, b = b, a % b
    return a


def compute_mod_inverse(e, phi_n):
    # Compute the modular multiplicative inverse of a number
    x, y, u, v = 0, 1, 1, 0
    while e != 0:
        q, r = phi_n // e, phi_n % e
        m, n = x - u * q, y - v * q
        phi_n, e, x, y, u, v = e, r, u, v, m, n
    return x % phi_n


def encrypt(message, public_key):
    # Encrypt the message using the public key
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message


def decrypt(encrypted_message, private_key):
    # Decrypt the encrypted message using the private key
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return "".join(decrypted_message)


# Step 1: Generate two large prime numbers, p and q
p = generate_prime()
q = generate_prime()

# Step 2: Compute n = p * q
n = p * q

# Step 3: Compute the totient function of n, phi(n) = (p - 1) * (q - 1)
phi_n = (p - 1) * (q - 1)

# Step 4: Select an encryption exponent e, which is a positive integer coprime to phi(n)
e = random.randint(2, phi_n)
while compute_gcd(e, phi_n) != 1:
    e = random.randint(2, phi_n)

# Step 5: Compute the decryption exponent d, which is the modular multiplicative inverse of e modulo phi(n)
d = compute_mod_inverse(e, phi_n)

# Public key: (e, n)
public_key = (e, n)

# Private key: (d, n)
private_key = (d, n)

# The message to be encrypted
message = input("Enter the message: ")

# Encryption
encrypted_message = encrypt(message, public_key)
print("Encrypted message:", encrypted_message)

# Decryption
decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted message:", decrypted_message)