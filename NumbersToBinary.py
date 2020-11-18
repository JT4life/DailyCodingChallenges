def intToBinString(a,b):
    strVal = ""
    if a+b == 0:
        return "0"
    while a+b > 0:
        if a+b % 2 != 0:
            strVal + "1"
        else:
            strVal + "0"
            a+b // 2
    return strVal

print(intToBinString(1000,111))