def find_words_starting_with_a_or_e(input_string):
    words = input_string.split()  # Split the input string into words
    result = []  # Initialize an empty list to store words starting with 'a' or 'e'
    for word in words:  # Iterate over each word
        if word.lower().startswith('a') or word.lower().startswith('e'):  # Check if word starts with 'a' or 'e'
            result.append(word)  # If yes, add it to the result list
    return result

# Example usage:
input_string = "An apple and an elephant are in the room."
words_starting_with_a_or_e = find_words_starting_with_a_or_e(input_string)
print("Words starting with 'a' or 'e':", words_starting_with_a_or_e)
