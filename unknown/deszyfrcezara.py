def caesar_decrypt(ciphertext, key):
    decrypted_text = ""
    
    for char in ciphertext:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - offset - key) % 26 + offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text

ciphertext = input("Podaj szyfrogram: ")
key = int(input("Podaj klucz: "))

print("Odszyfrowany tekst:", caesar_decrypt(ciphertext, key))
