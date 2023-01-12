message = input("Enter a message: ")

for check in range(len(message)):
    count = 0
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
        count += 1
        continue
    if count == len(message):
        print("ther is no capital letters")
    else:
        break
