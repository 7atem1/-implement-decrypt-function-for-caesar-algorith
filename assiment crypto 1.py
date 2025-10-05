def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    
    for char in ciphertext:
        if char.isalpha():  
            base = ord('A') if char.isupper() else ord('a')
           
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  
            
    return decrypted_text



cipher = "Khoor Zruog"  
print(caesar_decrypt(cipher, 3)) 
