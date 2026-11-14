def encryption(keysize, key, plaintext):
    # Ensure the plaintext length is divisible by keysize by adding 'x' padding if needed
    while len(plaintext) % keysize != 0:
        plaintext += 'x'

    cipher_text = ''

    # Encrypt by rearranging the plaintext based on the key
    for i in range(keysize):
        for j in range(len(plaintext)):
            if (j % keysize) + 1 == key[i]:
                cipher_text += plaintext[j]

    return cipher_text


if __name__ == "__main__":
    keysize = 4
    key = [3, 1, 2, 4]
    plaintext = input("Enter the plain text: ")

    ciphertext = encryption(keysize, key, plaintext)
    print("The encrypted text:", ciphertext)
