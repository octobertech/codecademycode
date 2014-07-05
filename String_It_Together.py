def reverse(text):
    """takes a string text and returns that string in reverse.""" 
    result=""
    for i in text:
        result=i+result
    return result
    
    
def anti_vowel(text):
    """takes a string text and returns the text with all of the vowels removed."""
    result=""
    for i in text:
        if i in "aeiouAEIOU":
            pass
        else:
            result+=i
    return result


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    """takes a string word as input and returns the equivalent scrabble score for that word."""
    result=0
    for i in word.lower():
        result+=score[i]
    return result


def censor(text, word):
    """takes two strings, text and word, as input and returns the text with the word you chose replaced with asterisks."""
    result = ""
    prep = text.split()
    list_pos_counter = 0
    for i in prep:
        if i == word:
            prep[list_pos_counter] = "*" * len(word)
        list_pos_counter += 1
    result = " ".join(prep)
    return result
