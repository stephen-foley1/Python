# Given large integer
large_int = int('340729841873182715861397179830856685654259321469692096127599848700034616712989535822328482917313631271598534498956022105309715286325299982013279476538056591160110165234154673739790739055092222057941412390792396213095811103894699574920250324039897163263561')

# Determine the appropriate number of bytes to decode
# The length of bytes will be derived from the bit length of the integer
byte_length = (large_int.bit_length() + 7) // 8  # Number of bytes needed

# Convert the large integer into a byte string
byte_data = large_int.to_bytes(byte_length, 'big')

# Decode the byte string into ASCII string
decoded_string = byte_data.decode('utf-8', errors='ignore')


# Reverse the decoded string to get the correct message
corrected_string = decoded_string[::-1]
print(" The Result is: ",decoded_string)
print("This appears to be backwords so heres the decoded string reversed :",corrected_string)

