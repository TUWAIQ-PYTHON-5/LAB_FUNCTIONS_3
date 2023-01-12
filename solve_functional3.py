
def string_function(word:str):
    if type(word) != str :
        return None
    temp:str =""
    for char in word :
         if char.isupper():
              temp += " "+char.lower()
         else:
            temp +=char
    return temp
print(string_function("HelloWorld"))
            