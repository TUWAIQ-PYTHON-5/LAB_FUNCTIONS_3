def kayword(word:str)-> str:   
  if type(word) !=str:
    return None
  else:
    tem:str=""

    for char in word:
        if char.isupper():
            tem +=" "+char.lower()
        else:
            tem+=char
    return tem
print(kayword("helloWord"))            