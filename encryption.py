# Function to process the string (split and swap characters)
def process_string(input_string):
	input_string = input_string.replace(" ", "")  # Remove spaces
	if len(input_string) % 2 != 0:
		input_string += 'x'  # Make even if odd length
	result = [input_string[i + 1] + input_string[i] for i in range(0, len(input_string) - 1, 2)]
	return ''.join(result)  # Return as a single string


# AutoKey Vigenère encryption
def autokey_vigenere_encrypt(plain_text, key):
	result = ""
	j = 0
	for i in range(len(plain_text)):
		char = plain_text[i]
		if char == ' ':
			result += ' '
		else:
			kChar = key[j]
			z = chr(((ord(char) - ord('A')) + (ord(kChar) - ord('A'))) % 26 + ord('A'))
			result += z
			j += 1  # Increment key index if not space
	return result


# Caesar Cipher with two keys (k1 for first char, k2 for second)
def caesar_cipher_two_keys(input_string, k1, k2):
	result = ""
	for i in range(0, len(input_string), 2):
		char1 = input_string[i]
		char2 = input_string[i + 1]
		encrypted_char1 = chr((ord(char1) - ord('A') + k1) % 26 + ord('A'))
		encrypted_char2 = chr((ord(char2) - ord('A') + k2) % 26 + ord('A'))
		result += encrypted_char1 + encrypted_char2
	return result


# Function to store in 2D array, input row by row, and display column by column (in one line)
def store_and_display_column_by_column(final_encrypted_string):
	# Split the string into two rows
	n = len(final_encrypted_string) // 2
	row1 = final_encrypted_string[:n]
	row2 = final_encrypted_string[n:]

	# Create a 2D array to store the rows
	matrix = [list(row1), list(row2)]

	# Display column by column in one line
	print("\nDisplaying by column (in one line):")
	for col in range(n):
		print(matrix[0][col] + matrix[1][col], end='')

	print()  # New line after the loop


# Main program
data = input("Enter the data to encrypt: ").upper()

# Step 1: Process the string (split and swap characters)
processed_data = process_string(data)
print(f"Processed data after splitting and swapping: {processed_data}")

# Step 2: Get the key for AutoKey Vigenère encryption
key = input("Enter the key: ").upper()

# Ensure the key length matches the input length for AutoKey Vigenère
if len(key) < len(processed_data):
	q = len(processed_data) - len(key)
	for i in range(q):
		if processed_data[i] != " ":
			key += processed_data[i]

# Step 3: AutoKey Vigenère encryption
encrypted_data = autokey_vigenere_encrypt(processed_data, key)
print(f"Encrypted data with AutoKey Vigenère: {encrypted_data}")

# Step 4: Apply Caesar Cipher with two keys
k1 = int(input("Enter the first Caesar key (k1): "))
k2 = int(input("Enter the second Caesar key (k2): "))

# Apply Caesar Cipher to the result of AutoKey Vigenère encryption
final_encrypted_string = caesar_cipher_two_keys(encrypted_data, k1, k2)
print(f"Final encrypted string after applying Caesar Cipher: {final_encrypted_string}")

# Step 5: Store the result in an array and display column by column (in one line)
store_and_display_column_by_column(final_encrypted_string)