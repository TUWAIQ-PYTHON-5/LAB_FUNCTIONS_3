def charctar(word):
    if(type(word) != str):
        return None
    else:
        for X in word:
            if X.isupper() == True:
                print("" , X.lower() , end="")
            elif X.islower() ==True:
                print(X , end="" )
charctar(input("enter word:"))

