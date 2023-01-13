# LAB_FUNCTIONS_3

## write a function that takes a string as a parameter
#- first check that the type of the parameter is of type str
#- then, it should separates the word at any capital letter and replace it with a small letter 
#- and  should return the new modified string !

#Example: helloWorld --> hello world


def check_string (sentence :str ) -> str :
    if type(sentence) != str :
       print("error")

    new_sentance = ""
    for i in sentence :
         if i.isupper():
          new_sentance =new_sentance +" "+i.lower()
         else :
            new_sentance = new_sentance + i 
    return new_sentance



        


    
print(check_string("welcomeNadaAlbuti"))
