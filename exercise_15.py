def letters(string):
    letters = {}

    for letter in string:
        if letter != " ":
            letter = letter.lower() 
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    return letters
string = input("Enter words: ")