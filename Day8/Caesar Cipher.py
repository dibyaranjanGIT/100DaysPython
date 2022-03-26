alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message : \n").lower()
shift = int(input("Type the shift : \n"))


def encrypt(plain_text='', shift=0):
    encrypt_message = []
    for letter in plain_text:
        original_position = alphabet.index(letter)
        new_position = original_position + shift
        if new_position > 25:
            new_position -= 26
        encrypt_message.append(alphabet[new_position])
    message = ''.join(encrypt_message)
    print(f"Encrypted {message}")


encrypt(text, shift)


def decrypt(plain_text='', shift=0):
    decrypt_message = []
    for letter in plain_text:
        original_postion = alphabet.index(letter)
        new_position = original_postion - shift
        if new_position < 0:
            new_position += 26
        decrypt_message.append(alphabet[new_position])
    message = ''.join(decrypt_message)
    print(f"Decrypted {message}")


decrypt(text, shift)
