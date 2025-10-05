def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    
    for char in ciphertext:
        if char.isalpha():  # Check if the character is a letter
            base = ord('A') if char.isupper() else ord('a')
            # Shift character backward and wrap around the alphabet
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # Keep non-letters unchanged
            
    return decrypted_text


# Example usage
cipher = "Khoor Zruog"   # "Hello World" encrypted with shift 3
print(caesar_decrypt(cipher, 3))  # Output: Hello World
