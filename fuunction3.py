
def myString(message):
    if type(message) == str:
        count = 0
        for check in range(len(message)):
            check2 = message[check]
            if check2.isupper():
                result = ""
                for letter in range(len(message)):
                    letter2 = message[letter]
                    if letter2.isupper():
                        result = result +" "+ letter2.lower()
                    else:
                        result = result + letter2
                print(result)        
            else:
                count = count + 1
                continue
        if count == len(message):
            print("ther is no capital letters")
        else:
            return
    else:
        print("the message is not valid")

message = input("Enter a message: ")
myString(message)