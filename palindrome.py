#---Check if a word is palindrome---#

def palindrome(word):
    new_word = word[::-1]

    if new_word == word:
        print(True)
    else:
        print(False)
    
palindrome()