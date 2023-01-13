def string_function (state: str):
    if not isinstance(state,str):
        return None
 
    temp : str=""
    for char in state :
        if char.isupper ():
            temp += " " + char.lower()
        else:
            temp += char
    return temp
print(string_function("saraAlotaibi"))