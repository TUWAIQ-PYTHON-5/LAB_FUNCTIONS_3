
def check(word :str):
    if type(word )!= str:
      return None
    
    mword=""
    for char in word:
            if char .isupper():
                mword+=" "+ char.lower()
            else:
                    mword+=char
    return mword
print(check("raghadNasser"))


