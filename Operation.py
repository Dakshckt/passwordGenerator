
def charGenerate():
    charValues = []
    for j in range(65 , 91):
        charValues.append(j)
    for k in range(97 , 123):
        charValues.append(k)
    return charValues

def numGenerate():
    numValues = []
    for i in range(48 , 57):
        numValues.append(i)
    return numValues

def specialGenerate():
    specialValues = []
    for k in range(32 , 48):
        specialValues.append(k)
    for k in range(57 , 65):
        specialValues.append(k)
    for k in range(91 , 97):
        specialValues.append(k)
    for k in range(123 , 127):
        specialValues.append(k)
    return specialValues

def allGenerate():
    values = []
    for i in range(32 , 126):
        values.append(i)
    return values

def txtGenerate(specificValue):
    result = ''
    for i in specificValue:
        result += chr(i)
    return result