"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print out every item in a list of items."""

    for item in items:
        print(item)


def get_all_evens(nums):
    """Given a list of numbers, return a list of all even numbers."""

    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums


def get_odd_indices(items):
    """Given a list, return all items at odd-numbered indices."""

    result = []

    for idx in range(len(items)):
        if not idx % 2 == 0:
            result.append(items[idx])

    return result 


def print_as_numbered_list(items):
    """Given a list, print a numbered list of the items."""

    i = 1

    for item in items:
        print(f'{i}. {item}')

        i += 1


def get_range(start, stop):
    """Return a list of numbers in a given range."""

    nums = []

    for num in range(start, stop):
        nums.append(num)

    return nums


def censor_vowels(word):
    """Given a string, return a string where vowels are replaced with '*'."""

    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)

    return ''.join(chars)


def snake_to_camel(string):
    """Given a string in snake case, return a string in upper camel case."""

    camelCase = []

    for word in string.split('_'):
        camelCase.append(f'{word[0].upper()}{word[1:]}')

    return ''.join(camelCase)


def longest_word_length(words):
    """Return the length of the longest word in a given list of words."""

    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest


def truncate(string):
    """Truncate repeating characters into one character."""

    result = []

    for char in string:
        if len(result) == 0 or not char == result[len(result) - 1]:
            result.append(char)

    return ''.join(result)


def has_balanced_parens(string):
    """Return true if all parentheses in a given string are balanced."""

    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1

            if parens < 0:
                return False

    return parens == 0


def compress(string):
    """Return the compressed version of a given string."""

    compressed = []

    currChar = ''
    charCount = 0

    for char in string:
        if not char == currChar:
            compressed.append(currChar)

            if charCount > 1:
                compressed.append(str(charCount))

            currChar = char
            charCount = 0

        charCount += 1

    compressed.append(currChar)
    if charCount > 1:
        compressed.append(str(charCount))

    return ''.join(compressed)
