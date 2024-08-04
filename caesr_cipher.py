def caesar_cipher(text, shift, mode):
  """Encrypts or decrypts a text using the Caesar Cipher.

  Args:
    text: The text to be encrypted or decrypted.
    shift: The number of positions to shift the letters.
    mode: The mode of operation, either 'encrypt' or 'decrypt'.

  Returns:
    The encrypted or decrypted text.
  """

  result = ""
  # Traverse the text
  for char in text:
    # Encrypt uppercase characters
    if char.isupper():
      char_code = ord(char)
      char_code = (char_code - 65 + shift) % 26
      result += chr(char_code + 65)
    # Encrypt lowercase characters
    elif char.islower():
      char_code = ord(char)
      char_code = (char_code - 97 + shift) % 26
      result += chr(char_code + 97)
    else:
      # Leave spaces and punctuation unchanged
      result += char
  return result

# Get input from the user
text = input("Enter your text: ")
shift = int(input("Enter the shift value (1-25): "))
mode = input("Enter mode (encrypt/decrypt): ")

# Check if mode is valid
if mode not in ['encrypt', 'decrypt']:
  print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
  exit()

# Perform encryption or decryption
if mode == 'encrypt':
  result = caesar_cipher(text, shift, mode)
  print("Encrypted text:", result)
elif mode == 'decrypt':
  result = caesar_cipher(text, -shift, mode)  # Decryption is the same as encryption with negative shift
  print("Decrypted text:", result)
