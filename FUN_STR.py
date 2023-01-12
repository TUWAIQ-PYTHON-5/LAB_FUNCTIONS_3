def function_str(string:str):
    if not isinstance(string, str):
        return None  

    null:str= ""
    for char in string:
         if char.isupper():
            null +=" " + char.lower()
         else:
            null+=char
    return null

print(function_str("HiEveryone"))

