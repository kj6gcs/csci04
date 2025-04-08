#*************************************************************************
# Your Name:           Robby Wideman
# Project Due Date:    04-09-2025
# Project Name:        Project 5: Cipher
# CSCI-4: Intro to Programming
# Spring 2025
# Project Description: A program which takes input from a user and encrypts
# it based on a cipher shift key (also provided by the user), and returns
# the encrypted value. Can also decrypt.
#*************************************************************************

# Write your code under this line *******************************************

# I wanted to do something a little different, moreso to get a user's attention, so I'm adding color 
# options to change terminal output text for different things:
# ANSI escape codes for colors
RED         = "\033[91m"
GREEN       = "\033[92m"
YELLOW      = "\033[93m"
CYAN        = "\033[96m"
BLUE        = "\033[34m"
BRIGHTBLUE  = "\033[94m"
BRIGHTRED   = "\033[91m"
ORANGE      = "\033[38;5;208m"
MAGENTA     = "\033[35m"
ITALIC      = "\033[3m"     # Adding some "style" to it!
RESET       = "\033[0m"     # This has to be used after each time the text is altered to reset the text back to it's baseline.


# Encryption function:
def encrypt(text, shift):
    encrypted = ""
    for char in text:
        # Converts character to ASCII number, adds the shift key from user, wrap around with 
        # modulo 127 (the printable ASCII range ends at 126):
        new_char = chr((ord(char) + shift) % 127)
        encrypted += new_char
    return encrypted # Sends out the encrypted value/string.

# I wanted to give users the option of taking an encrypted string and decoding it, so here's the-
# Decryption function:
def decrypt(text, shift):
    decrypted = ""
    for char in text:
        # Subtract shift and wrap around using modulo, like the encrypt function but the opposite
        new_char = chr((ord(char) - shift) % 127) # We use the "- shift" here to reverse the encryption based on the user-provided key.  
                                                  # This "undoes" the encryption if the same key is used.
        decrypted += new_char
    return decrypted # Sends out the decrypted value/string


# Initial welcome message:
print(BRIGHTBLUE + ITALIC + "\n>>>" + BRIGHTRED + "Robby's Radical" + BRIGHTBLUE + " Caeser Cipher" + BRIGHTRED + "<<<\n" + RESET)
print(ORANGE + "This is a simple Caesar/Shift Cipher Encoder/Decoder\n" + RESET)
print(RED + "You'll first select if you want to encrypt, decrypt, or quit.\n" + RESET)
print(BLUE + "From there, you'll enter the text to encrypt/decrypt, followed by the Cipher Key you want to use.\n" + RESET)
print(MAGENTA + "Remember what Cipher Key you use if you wish to decrypt your message in the future!\n" + RESET)


# Starting a loop of the program, this way the program runs until the user selects "Q/q" when prompted or closes the program:
while True:

    # Asking the user if they want to encrypt, decrypt, or quit:
    action = input(BLUE + "\nWould you like to (E)ncrypt, (D)ecrypt, or (Q)uit? " + RESET).strip().lower()

    # Exit if user chooses to quit the program:
    if action == 'q':
        print(RED + "Goodbye!" + RESET)
        exit()

# Validate action before proceeding
    if action not in ['e', 'd']:
        print(RED + "Invalid option. Please choose to (E)ncrypt, (D)ecrypt, or (Q)uit." + RESET)
        continue

    # Now safe to proceed with the rest:
    message = input(YELLOW + "Please type the word or phrase you wish to encrypt/decrypt: " + RESET)


    # Display message back to user (from their plaintext input OR encrypted input):
    print(YELLOW + "Text to Encrypt/Decrypt: " + message, RESET)

    # Loop to ensure valid integer input for cipher shift key value:
    while True:
        try:
            shift = int(input(YELLOW + "Please type the shift value you want to use (Cipher Key): " + RESET)) # This takes a whole number 
                                                                                                                # input (integer) from the user to use as the cipher key:
            break
        except ValueError: # If the user puts in a decimal number or non-numeral character, they will receive this message to help correct the issue:
            print(RED + "Whoops! This needs to be a whole number with no decimal places!" + RESET)

    # Process based on user's action selection:
    # This tells the program to encrypt if the user inputs E/e in the action input phase, using the functions above:
    if action == 'e':
        result = encrypt(message, shift)
        print(GREEN + "Encrypted Message: 🔒 " + result, RESET)
    # This tells the program to decrypt if the user inputs D/d in the action input phase, using the functions above:
    elif action == 'd':
        result = decrypt(message, shift)
        print(CYAN + "Decrypted Message: 🔓 " + result, RESET)
    # If a user does not input an E/e, D/d, or Q/q in the action input phase, this message will display:
    else:
        print(RED + "Invalid option. Please choose to (E)ncrypt, (D)ecrypt, or (Q)uit." + RESET) # If a user selects something outside of the valid choices, they receive this message.
        continue # Then, the loop starts over looking for correct input.
