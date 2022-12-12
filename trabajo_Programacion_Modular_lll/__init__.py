""" Design a function called charactersInString that has a character string and a character
as input parameters and returns how many times that character appears in the string. It
should do it no matter if the string and character are lower case or upper case characters."""

def charactersInString(character, string):
    count=0
    for i in range(len(string)):
        if character.upper() == string[i].upper():
            count+=1
    return count

print(charactersInString("o", "holo mundo como estais"))