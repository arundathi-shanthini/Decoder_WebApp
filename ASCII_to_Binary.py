# Read the message
with open("message_to_decode.txt") as f:
   message=list(f.read())

# Encode the message
encoded_message = [bin(ord(letter))[2:] for letter in message]
encoded_message = ' '.join(['0'*(8-len(letter))+letter for letter in encoded_message])

# Display the message
print(encoded_message)

# Write message to output file
with open('output.txt', 'w') as f:  
    f.write(encoded_message)
