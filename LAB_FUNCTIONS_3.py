## write a function that takes a string as a parameter
# - first check that the type of the parameter is of type str
# - then, it should separates the word at any capital letter and replace it with a small letter 
# - and  should return the new modified string !

# Example: helloWorld --> hello world

def separate(word : str):
    result = ""
    if type(word) != str :
        return "The input should be string "
    for char in word :      
        if char.isupper() :
            lower=char.lower()
            result = result + " " + lower 

        else :
            result = result + char  
    return result



print(separate("helloWorld"))
