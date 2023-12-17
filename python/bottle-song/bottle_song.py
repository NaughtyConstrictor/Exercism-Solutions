NUMS = "one two three four five six seven eight nine ten".split()

def recite_verse(num):
    if num == 1:
        return [
            "One green bottle hanging on the wall,",
            "One green bottle hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be no green bottles hanging on the wall.",
            "",
        ]
        
    if num == 2:
        return [
            "Two green bottles hanging on the wall,",
            "Two green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be one green bottle hanging on the wall.",
            "",
        ]
        
    num_1 = NUMS[num - 1].capitalize()
    num_2 = NUMS[num - 2]
    return [
        f"{num_1} green bottles hanging on the wall,",
        f"{num_1} green bottles hanging on the wall,",
        f"And if one green bottle should accidentally fall,",
        f"There'll be {num_2} green bottles hanging on the wall.",
        "",
    ]
    
    

def recite(start, take=1):
    verses = []
    for i in range(take):
        verses.extend(recite_verse(start - i))
    return verses[:-1]