def reversing_string(str):
    reversed_string = ""
    for char in str:
        reversed_string = char + reversed_string

    words = str.split()  # Split the input string into words
    length = [len(word) for word in words]  # Get the length of each word

    result = []
    start_index = 0
    for l in length:
        # Extract each word from the reversed string
        reversed_word = reversed_string[start_index:start_index + l]
        result.append(reversed_word)
        start_index += l

    # Join the reversed words with spaces to form the final output string
    return " ".join(result)

# Example usage
str = "i hate python coding"
output_string = reversing_string(str)
print(output_string)  # Output: "g nido cnohty prtahi"
