import random
def permutation_example(word):
    word_list = list(word)
    random.shuffle(word_list)
    shuffled_word = ''.join(word_list)
    return shuffled_word
input_word = "Python"
result = permutation_example(input_word)
print(result)