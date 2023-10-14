def pig_latin(word):
    vowels_1 = ("xr", "yt", "a", "e", "i", "o", "u")
    vowels_2 = {"a", "e", "i", "o", "u", "y"}
    
    if word.startswith(vowels_1):
        return word + "ay"
    if word[0] == "y":
        return word[1:] + "yay"
    
    qu_index = word.find("qu")
    if qu_index != -1:
        return word[qu_index + 2:] + word[:qu_index] + "quay"
    
    for i, char in enumerate(word):
        if char in vowels_2:
            break
    
    return word[i:] + word[:i] + "ay"
    
def translate(text):
    return " ". join(pig_latin(word) for word in text.split())