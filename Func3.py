
def checkWord(words : str):
    words.split(',')
    if type(words) != str : 
        print("input is Not a string")
         

    for letter  in words:
        if letter == letter.upper():
            print("" , end=" ")

        print(letter.lower(), end="")
        

checkWord("helloWorldFahadAlpha")