def sentence (txtInput : str):

        for char in txtInput:
            if (char.islower() == True):
                print(char,end='')
            else: 
                print('',char.lower(),end='')

        print()


usrtxt : str = str(input("Input Your Text:"))
sentence(usrtxt)