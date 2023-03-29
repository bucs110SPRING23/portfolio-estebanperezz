def caesar_cipher(text,factor):
    result = ""
    for char in text:
        if char.isalpha():
               # Determine the case of the character
            start = ord('A') if char.isupper() else ord('a')
            # Calculate the new position of the character after the shift
            shift = factor * (13*factor) + 7 
            new_pos = (ord(char) - start + shift) % 26
            # Convert the new position back to a character
            char = chr(start + new_pos)
        result += char
    return result
msg = caesar_cipher("The quick brown fox jumps over the lazy dog",5)
encrypted = open("encrpyted.txt", "w")
encrypted.write(msg)

