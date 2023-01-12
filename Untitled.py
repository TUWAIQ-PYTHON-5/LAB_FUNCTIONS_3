def checekworld(word):
    if type(word) != str:
        return None

    temp:str=""

    for char in word:
        if char.isupper():
            temp+= " "+char.lower()
        else:
            temp+=char
        return temp


print(checekworld("helloWorld"))