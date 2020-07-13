import re
import sys

def sorted_count_words():
    """Count how many times each space-separated word occurs in that file"""

    file = open(str(sys.argv[1]))

    word_count = {}

    for line in file: 
        words = line.split(" ")

        for word in words:
            regex = re.compile('[^a-zA-Z]')
            word = regex.sub('', word)
            word = word.lower()



            word_count[word] = word_count.get(word, 0) + 1

    highest_word_count = sorted(word_count.items(), 
        key=lambda x: x[1], reverse=True)   

    return highest_word_count

def count_words():
    """Return a sorted list with counts of how many times each 
    space-separated word occurs in that file (case insensitive)
    """

    file = open(str(sys.argv[1]))

    word_count = {}

    for line in file: 
        words = line.split(" ")

        for word in words:
            regex = re.compile('[^a-zA-Z]')
            word = regex.sub('', word)

            word_count[word] = word_count.get(word, 0) + 1


    return word_count

print(count_words())
print(sorted_count_words())
