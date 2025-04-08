import string

# Get all printable characters (letters, digits, punctuation, whitespace)
printable_chars = string.printable  # Contains 100 printable ASCII characters

# Encryption function for all printable characters
def encrypt(text, shift):
    result = ""
    for char in text:
        if char in printable_chars:
            index = printable_chars.index(char)
            shifted_index = (index + shift) % len(printable_chars)
            result += printable_chars[shifted_index]
        else:
            result += char  # Leave non-printable chars untouched (just in case)
    return result

# Decryption function
def decrypt(text, shift):
    return encrypt(text, -shift)

# Ask user what they want to do
action = input("Would you like to (E)ncrypt or (D)ecrypt? ").strip().lower()

# Get message and shift key
message = input("Please type the string: ")
shift = int(input("Please type the shift value you want to use (Cipher Key): "))

# Encrypt or decrypt
if action == 'e':
    encrypted = encrypt(message, shift)
    print("Encrypted text:", encrypted)
elif action == 'd':
    decrypted = decrypt(message, shift)
    print("Decrypted text:", decrypted)
else:
    print("Invalid option. Please enter 'E' or 'D'.")
