import re
import sys
from collections import Counter


def count_words():
    """Count how many times each space-separated word occurs in that file"""

    file = open(str(sys.argv[1]))

    word_count = {}

    for line in file: 
        words = line.split(" ")

        for word in words:
            word = word.lower()
            regex = re.compile('[^a-z]')
            word = regex.sub('', word)

            word_count[word] = word_count.get(word, 0) + 1


    return word_count



def sorted_count_words():
    """Return a sorted list with counts of how many times each 
    space-separated word occurs in that file (case insensitive)
    """

    word_count = count_words()

    highest_word_count = sorted(word_count.items(), 
        key=lambda x: x[1], reverse=True)   

    return highest_word_count



def sorted_count_words_trickier():
    """Return a sorted list with counts of how many times each 
    space-separated word occurs in that file ordered alphabetically 
    (case insensitive)
    """

    highest_word_count = sorted_count_words()

    high_count = highest_word_count[0][1]

    highest_word_count_alpha = []
    temp = []
    num = high_count

    while num >= 1:

        for word in highest_word_count:

            if word[1] == num:
                temp.append(word)

        highest_word_count_alpha.extend(sorted(temp, key=lambda x: x[0]))

        temp = []
        num -= 1

    return highest_word_count_alpha


# Changed to using collections here

def using_collections_counter():

    words = re.findall(r'\w+', open(str(sys.argv[1])).read().lower())
    
    highest_word_count = Counter(words).most_common()

    return sort_by_count_then_alpha(highest_word_count)



def sort_by_count_then_alpha(highest_word_count):

    high_count = highest_word_count[0][1]

    highest_word_count_alpha = []
    temp = []
    num = high_count

    while num >= 1:

        for word in highest_word_count:

            if word[1] == num:
                temp.append(word)

        highest_word_count_alpha.extend(sorted(temp, key=lambda x: x[0]))

        temp = []
        num -= 1

    return highest_word_count_alpha


# print(count_words())
# print(sorted_count_words())
# print(sorted_count_words_trickier())
print(using_collections_counter())

