'''
# LAB_FUNCTIONS_3

## write a function that takes a string as a parameter
- first check that the type of the parameter is of type str
- then, it should separates the word at any capital letter and replace it with a small letter 
- and  should return the new modified string !

Example: helloWorld --> hello world'''

def sentence (txtInput : str):
    #if (type(txtInput) != type("Hello")):
       # print("Try again with text ")
    #else:
        #for txtInput in range(txtInput):
        for char in txtInput:
            if (char.islower() == True):
                print(char,end='')
                #print("Test")
            else: 
                print('',char.lower(),end='')
            #if (islower(rewright)

        print()


#print(type("hello"))
usrtxt : str = str(input("Input Your Text:"))
sentence(usrtxt)