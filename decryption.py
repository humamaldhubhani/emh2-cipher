# Function to reverse the string splitting and swapping
def reverse_process_string(input_string):
	result = [input_string[i + 1] + input_string[i] for i in range(0, len(input_string) - 1, 2)]
	return ''.join(result)


# Caesar Cipher decryption with two keys
def caesar_cipher_two_keys_decrypt(input_string, k1, k2):
	result = ""
	for i in range(0, len(input_string), 2):
		char1 = input_string[i]
		char2 = input_string[i + 1]
		decrypted_char1 = chr((ord(char1) - ord('A') - k1 + 26) % 26 + ord('A'))
		decrypted_char2 = chr((ord(char2) - ord('A') - k2 + 26) % 26 + ord('A'))
		result += decrypted_char1 + decrypted_char2
	return result


# New AutoKey Vigenère decryption with user input logic
def autokey_vigenere_decrypt(ciphertext, keyword):
	# Convert keyword to a list and prepare to generate the full key
	key = list(keyword)
	plaintext = []

	# Loop over each character in the ciphertext
	for i in range(len(ciphertext)):
		# If the key length is less than the ciphertext length, add the already decrypted plaintext
		if i >= len(keyword):
			key.append(plaintext[i - len(keyword)])

		# Decrypt each character: (Ciphertext - Key) mod 26
		decrypted_char = chr((ord(ciphertext[i]) - ord(key[i]) + 26) % 26 + ord('A'))
		plaintext.append(decrypted_char)

	return "".join(plaintext)


# Function to input the ciphertext column by column and then display row by row
def input_column_by_column(ciphertext):
	n = len(ciphertext) // 2  # Divide ciphertext into 2 rows
	matrix = [[''] * n for _ in range(2)]  # Create an empty 2D array with 2 rows

	# Fill the matrix column by column
	idx = 0
	for col in range(n):
		matrix[0][col] = ciphertext[idx]
		matrix[1][col] = ciphertext[idx + 1]
		idx += 2

	# Display the matrix row by row
	print("\nDisplaying row by row:")
	for row in matrix:
		print(''.join(row))

	# Return the matrix as a concatenated string (row by row)
	return ''.join(matrix[0]) + ''.join(matrix[1])


# Complete decryption process (reverses all steps)
def decrypt(final_encrypted_string, key, k1, k2):
	# Step 1: Input column by column, then display row by row
	print("Step 1: Input column by column, then display row by row")
	decrypted_string = input_column_by_column(final_encrypted_string)
	print(f"Intermediate result after step 1: {decrypted_string}\n")

	# Step 2: Reverse Caesar Cipher decryption
	print("Step 2: Apply Caesar Cipher decryption")
	decrypted_data = caesar_cipher_two_keys_decrypt(decrypted_string, k1, k2)
	print(f"Intermediate result after step 2: {decrypted_data}\n")

	# Step 3: Reverse AutoKey Vigenère decryption
	print("Step 3: Apply AutoKey Vigenère decryption")
	autokey_decrypted_string = autokey_vigenere_decrypt(decrypted_data, key)
	print(f"Intermediate result after step 3: {autokey_decrypted_string}\n")

	# Step 4: Reverse the string splitting and swapping
	print("Step 4: Apply reverse process string (swap back characters)")
	original_string = reverse_process_string(autokey_decrypted_string)
	print(f"Final decrypted result: {original_string}\n")

	return original_string


# Main decryption logic
data = input("Enter the encrypted data to decrypt (in column order): ").upper()
key = input("Enter the key: ").upper()
k1 = int(input("Enter the first Caesar key (k1): "))
k2 = int(input("Enter the second Caesar key (k2): "))

# Decrypt the data
decrypted_result = decrypt(data, key, k1, k2)
print(f"Decrypted result: {decrypted_result}")
