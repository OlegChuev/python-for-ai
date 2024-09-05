import re


def swap_words(text, N):
    # Split the text into words while preserving punctuation
    words = re.findall(r"\b\w+\b", text)

    # Check if N is within the valid range
    if N <= 0 or N > len(words):
        raise ValueError(
            "N should be greater than 0 and less than or equal to the number of words in the string"
        )

    # Calculate the position of the 20-N word
    M = 20 - N

    # Validate the 20-N position
    if M <= 0 or M > len(words):
        raise ValueError(
            "20-N should be greater than 0 and less than or equal to the number of words in the string"
        )

    # Get the words to swap
    word_n = words[N - 1]
    word_20_n = words[M - 1]

    # Create a regex pattern to match words in the text
    pattern = re.compile(r"\b\w+\b")

    # Replace the N-th and (20-N)-th words
    def replacement(match):
        word = match.group(0)
        index = words.index(word)

        if index == N - 1:
            return word_20_n
        elif index == M - 1:
            return word_n
        else:
            return word

    # Perform the replacements using the regex pattern
    new_text = pattern.sub(replacement, text)

    return new_text


# Prompt user for input
input_string = "Програміст — фахівець, що займається програмуванням, виконує розробку програмного забезпечення (в простіших випадках — окремих програм) для програмованих пристроїв, які, як правило містять один процесор чи більше"
N = int(input("Enter the number N: "))

# Swap words and display the result
result = swap_words(input_string, N)
print("Resulting string:", result)
