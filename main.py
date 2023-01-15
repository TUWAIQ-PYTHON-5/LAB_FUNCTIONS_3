'''LAB_FUNCTIONS_3

    ## write a function that takes a string as a parameter
    - first check that the type of the parameter is of type str
    - then, it should separates the word at any capital letter and replace it with a small letter 
    - and  should return the new modified string !

Example: helloWorld --> hello world
'''
def cutString(word : str):
    if(type(word) != str):
        return None
    else:
        strName = ""
        for i in word:
            if i.isupper():
                
                strName += f'{i.lower()} '
                 
            elif i.islower():
                strName += i
                 
    return strName
                    
                    
    



print(cutString(str(input("please enter Any word"))))          



                
                


