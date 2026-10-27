def clean_text(text):
    text = text.lower()
    punctuation = ".,!?;:'\"()-"
    for mark in punctuation:
        text = text.replace(mark, "")
    return text.split()


def count_words(words):
    return len(words)

def count_characters(text):
    text = text.replace(" ", "")
    return len(text)


def count_vowels(words):
    vowels = "aeiou"
    count = 0
    for word in words:
        for letter in word:
            if letter in vowels:
                count += 1
    return count


def count_consonants(words):
    vowels = "aeiou"
    count = 0
    for word in words:
        for letter in word:
            if letter.isalpha() and letter not in vowels: #isalpha() string method checks whether a string contains only alphabetic characters and has at least one character.
                count += 1
    return count


def find_longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def count_word_frequency(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


def find_repeated_words(frequency):
    repeated = []
    for word in frequency:
        if frequency[word] > 1:
            repeated.append(word)
    return repeated


def find_top_five(frequency):
    sorted_words = []
    for word in frequency:
        sorted_words.append(word)
    for i in range(len(sorted_words)):
        for j in range(i + 1, len(sorted_words)):
            if frequency[sorted_words[j]] > frequency[sorted_words[i]]:
                sorted_words[i], sorted_words[j] = sorted_words[j], sorted_words[i]
    return sorted_words[:5]


text = input("Enter a paragraph: ")
words = clean_text(text)
print("\n===== TEXT ANALYSIS=====")
print("Words:", count_words(words))
print("Characters excluding spaces:", count_characters(text))
print("Vowels:", count_vowels(words))
print("Consonants:", count_consonants(words))
print("Longest word:", find_longest_word(words))
frequency = count_word_frequency(words):
print("Word frequency:", frequency)
print("Repeated words:", find_repeated_words(frequency))
print("Five most frequent words:", find_top_five(frequency))