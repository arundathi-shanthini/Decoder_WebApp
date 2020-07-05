# Read the message
with open("message_to_encode.txt") as f:
    encoded_message=f.read().split()

# Decode the message
decoded_message = ''.join([chr(int(letter,2)) for letter in encoded_message])

# Display the message
print(decoded_message)
