from operator import index
def some_words (aword : str):
    if not (type(aword) == str):
        return None
    temp: str=" "
    for char in aword:
       if char.isupper():
        temp += " " + char.lower()
    else:
        temp += char
        return temp





print(some_words("helloWord"))

