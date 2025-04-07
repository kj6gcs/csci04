 #*************************************************************************
 # Your Name:           Robby Wideman
 # Project Due Date:    04-09-2025
 # Project Name:        Project 5: Cipher
 # CSCI-4: Intro to Programming
 # Spring 2025
 # Project Description: A program which takes input from a user and encrypts
 # it based on an encryption key provided by the user.  It then provides
 # an encryption of the input from the user.  It can also decrypt strings
 # back to the unencrypted state so long as the user inputs the correct
 # encrypted text and the same cipher key (salt) used during encoding.
 #*************************************************************************

#Write your code under this line*******************************************


import hashlib #importing this to have consistent encryption, as well as not just a simple shift cipher.
import random #using this also allows us to shuffle the ASCII values in a consistent way as well

PRINTABLE_CHARS = [chr(i) for i in range(32, 127)]  # 95 printable ASCII characters using this range

def build_substitution_maps(salt='cipher'):
    #Now we will build a consistent, one-to-one character substitution shift map by using the cipher key (salt).

    source = PRINTABLE_CHARS.copy()
    shuffled = PRINTABLE_CHARS.copy()

    seed = int(hashlib.sha256(salt.encode()).hexdigest(), 16) #this converts our cipher key (salt) into a hex number via SHA-256 hash/encryption
                                                                #which is then turned into a base-10 integer to use as our "seed"/key.
    random.Random(seed).shuffle(shuffled)   #This gives us a "random" shuffle of our input, but doesn't affect globally, just locally.

    forward = dict(zip(source, shuffled))
    reverse = dict(zip(shuffled, source))
    return forward, reverse

def encode_text(text, cipher_map):
    return ''.join(cipher_map.get(c, c) for c in text)

def decode_text(text, reverse_map):
    return ''.join(reverse_map.get(c, c) for c in text)

def main():
    print("=== Welcome to the Cipher Tool ===")

    while True:
        mode = input("\nWould you like to (E)ncrypt, (D)ecrypt, or (Q)uit?: ").strip().lower()
        if mode in ['q', 'quit']:
            print("Goodbye!")
            break
        elif mode not in ['e', 'd']:
            print("Invalid option. Please choose E, D, or Q.")
            continue

        text = input("Enter the text (or type 'q' to quit): ")
        if text.strip().lower() in ['q', 'quit']:
            print("Exiting...")
            break

        key = input("Enter your cipher key (or type 'q' to quit): ")
        if key.strip().lower() in ['q', 'quit']:
            print("Exiting...")
            break

        cipher_map, reverse_map = build_substitution_maps(key)

        if mode == 'e':
            result = encode_text(text, cipher_map)
            print(f"\nYou entered: {text}")
            print(f"With a cipher key of: {key}")
            print(f"🔒 Encrypted value: {result}")
        else:
            result = decode_text(text, reverse_map)
            print(f"\nYou entered: {text}")
            print(f"With a cipher key of: {key}")
            print(f"🔓 Decrypted value: {result}")

# this is where all the "magic" happens, taking everything above here and running it all!
if __name__ == "__main__":
    main()
