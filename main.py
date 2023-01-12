def checkWord(word:str):
    ''' This Function Will do Speaces between words '''
    if type(word)!=str:
        return None
    
    temp:str=""
    for char in word:
        if char.isupper():
            temp += " " + char.lower()
        else:
            temp += char
        word=temp
    return word

userWord=input("Enter Your Word : ")
print(checkWord(word=userWord))

