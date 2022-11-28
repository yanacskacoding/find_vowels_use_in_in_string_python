'''Define a function isVowel2(char) that returns True if char is a vowel ('a', 'e', 'i', 'o', or 'u'), and False otherwise. You can assume that char is a single letter of any case (ie, 'A' and 'a' are both valid).

This function is similar to the previous problem - but this time, do use the keyword in. Your function should take in a single string and return a boolean.

def isVowel2(char):

    ' ' '

    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.

    ' ' '

    # Your code here
char = input()

** Include input in your program like shown above.

Example:

 isVowel2('a')
    True
 isVowel2('A')
    True
isVowel2('.')
    False
isVowel2('Z')
    False
'''
#Code:
def remove_special_chars(thisString):
    return(''.join(e for e in thisString if e.isalnum()))

def isVowel(char):
    char = char.lower()
    if char.isalpha():
        letters = ['a','e','i','o','u']
        if char in letters:
            return True
        return False

char = input()
char = remove_special_chars(char)

print(isVowel(char))