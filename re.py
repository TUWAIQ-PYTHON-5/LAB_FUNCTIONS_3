
'''def sentence (txtInput : str):
    #if (type(txtInput) != type("Hello")):
       # print("Try again with text ")
    #else:
        #for txtInput in range(txtInput):
        for char in txtInput:
            

        print()'''

def reconstruct (char : str) -> str:
    if (char.islower() == True):
        rerun: str = (char + '')
        return rerun
                #print("Test")
    else:
        rerun : str = (' '+char.lower())
        return rerun
            #if (islower(rewright)

usrtxt : str = str(input("Input Your Text:"))
for char in usrtxt:
    print(reconstruct(char), end ='')