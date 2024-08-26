# Given string
input_string = "The quick brown fox jumps over the lazy dog"

# Split the string into words using whitespace as the delimiter
word_list = input_string.split()

# Initialize an empty list to store words longer than 3 characters
long_words = []

# Iterate through the words and add longer words to the 'long_words' list
for word in word_list:
    if len(word) > 3:
        long_words.append(word)

# Print the list of words longer than 3 characters
print("Words longer than 3 characters:", long_words)
