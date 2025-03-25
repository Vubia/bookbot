def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    # Sort the dictionary by values (character counts) in descending order
    sorted_characters = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True))
    return sorted_characters