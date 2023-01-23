def checekworld(word:str):
    if type(word) != str:
        return None
    else:

        temp:str=""

    for char in word:
        if char.isupper():
            temp+= " "+char.lower()
        else:
            temp+=char
        word=temp
    return temp


print(checekworld("helloWorld"))