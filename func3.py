
def charctar(word) -> str : 
    if(type(word) != str):
        return None
    else:
        for X in word:
            if X.isupper() == True:
                print("" , X.lower() , end="")
            elif X.islower() ==True:
              return X            
charctar(input("enter word:")) 