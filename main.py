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
        for i in word:
            if i.isupper() == True:
                print("" , i.lower() , end="")
            elif i.islower() ==True:
                print(i , end="" )    
            
            



cutString(str(input("please enter Any word")))             
                
                


