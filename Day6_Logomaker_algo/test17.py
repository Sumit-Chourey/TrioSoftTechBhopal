import itertools
from nltk.corpus import wordnet
import nltk

# Download the required WordNet data
nltk.download('wordnet')
nltk.download('omw-1.4')


#Giving synonmus and antonyms word using lemma (Natural Language Processing)
def get_synonyms_antonyms(word):
    synonyms = set()
    antonyms = set()
    
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
            if lemma.antonyms():
                antonyms.add(lemma.antonyms()[0].name())
    
    return list(synonyms), list(antonyms)


#Checking If that word presemnt in dictionary or Not 

def is_word_in_dictionary(word):
    return bool(wordnet.synsets(word))



#Bubble sorting taking place here....!

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


#Dividing string into valid parts validation checking using library

def divide_into_valid_substrings(input_string):
    substrings = set()
    n = len(input_string)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = input_string[i:j]
            if is_word_in_dictionary(substr):
                substrings.add(substr)
    return list(substrings)



#Perform Permutation, Combination, Antomyus, Synonyms

def process_substring(substring):
    # Get synonyms and antonyms
    synonyms, antonyms = get_synonyms_antonyms(substring)

    # Get permutations
    print("---------------------------------------------------------------------------------------")
    print(f"\nProcessing substring: {substring}")
    print("Permutations (valid words):")
    perms = []                                          #creating blank array
    if len(substring) > 2:                              #Checking substring (length > 2) 
        for perm in itertools.permutations(substring):  #divide into character
            perm_word = ''.join(perm)                   # form words using character
            if is_word_in_dictionary(perm_word):        #Checking that Word is present or not in dictionary
                perms.append(perm_word)
        bubble_sort(perms)                      #Sorting (Bubble Sort)
        for perm_word in perms:
            if len(perm_word)>2:                #checking lrngth of word after substring
                print(perm_word)
        print(f"\nTotal number of valid permutations: {len(perms)}")
    else:
        print("Substring length is less than or equal to 2. Permutations not generated.")
    print("---------------------------------------------------------------------------------------")
    
    
    
    # Get combinations
    print("---------------------------------------------------------------------------------------")
    print("Combinations (valid words):")
    combs = []
    if len(substring) > 2:
        for r in range(1, len(substring) + 1):
            for comb in itertools.combinations(substring, r):
                comb_word = ''.join(comb)
                if is_word_in_dictionary(comb_word):
                    combs.append(comb_word)
        bubble_sort(combs)
        for comb_word in combs:
            if len(comb_word)>2:
                print(comb_word)
        print(f"\nTotal number of valid combinations: {len(combs)}")
    else:
        print("Substring length is less than or equal to 2. Combinations not generated.")

    
    
    # Display synonyms
    print("---------------------------------------------------------------------------------------")
    print("Synonyms (valid words):")
    valid_synonyms = [synonym for synonym in synonyms if is_word_in_dictionary(synonym)]  #Creating List  and checking
    bubble_sort(valid_synonyms) 
    if valid_synonyms:
        for synonym in valid_synonyms:
            print(synonym)
    else:
        print("No synonyms found.")




    # Display antonyms
    print("---------------------------------------------------------------------------------------")
    print("Antonyms (valid words):")
    valid_antonyms = [antonym for antonym in antonyms if is_word_in_dictionary(antonym)]  #Creating List  and checking
    bubble_sort(valid_antonyms)
    if valid_antonyms:
        for antonym in valid_antonyms:
            print(antonym)
    else:
        print("No antonyms found.")


# Code starting Point is here ...

def get_permutations_and_combinations():
    # Get user input
    user_input = input("Enter a word: ")
    
    # Divide input into valid substrings
    valid_substrings = divide_into_valid_substrings(user_input)
    
    # Process each valid substring
    for substring in valid_substrings:
        if len(substring) > 2:
            process_substring(substring)

if __name__ == "__main__":
    get_permutations_and_combinations()
