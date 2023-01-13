user_inputt = str (input ("Enter Words :"))
def function(word: str) -> str:
    if type(word) != str:
       return None

    temp: str = ""

    for char in word:
        if char.isupper():
            temp += " " + char.lower()
        else:
            temp += char

    return temp
print(function(user_inputt))

