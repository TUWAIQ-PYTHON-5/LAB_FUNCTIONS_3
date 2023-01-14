def checkletters (hello:str):
    if isinstance(hello,str):
        return None

    temp:str = ""
    for i in hello:
        if i.isupper():
          temp += " "+ i.lower()
        else:
         temp += i
    return temp


print(checkletters("welcometoPython"))

