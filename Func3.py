
def checkWord(words : str):
    
    if type(words) != str : 
        print("input is Not a string")
        
    statement = ""
    for letter  in words:

        if letter == letter.upper():
             statement += " "+letter 
        else:
            statement += letter
    return statement.lower()

print(checkWord("helloWorldFahadAlpha"))