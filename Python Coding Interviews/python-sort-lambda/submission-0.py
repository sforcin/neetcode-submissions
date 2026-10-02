from typing import List

#to use lambda sorting: 
# we use key = lambda 
# word or any variable name we want to define the function in 
# : colon to define the function
# the expression you wanna use 

def sort_words(words: List[str]) -> List[str]:
    words.sort(key= lambda word: len(word), reverse = True)
    return words
    pass


def sort_numbers(numbers: List[int]) -> List[int]:
    pass


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
