
def checkWord(words : str):

    if type(words) != str : 
        print("input is Not a string")
        return None 

    for letter  in words:
        if letter == letter.upper():
            print("" , end=" ")

        print(letter.lower(), end="")

checkWord("helloWorld")