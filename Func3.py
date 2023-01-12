
def checkWord(words : str):
    setatement = ""
    if type(words) != str : 
        print("input is Not a string")
         
    for letter  in words:
        if letter == letter.upper():
             setatement += " "+letter 
        else:
            setatement += letter
    return setatement.lower()

print(checkWord("helloWorldFahadAlpha"))