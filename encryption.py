
def encryption3(encryptedCode):
    newstr = encryptedCode.replace("a","x")
    newstr = newstr.replace("j","5g")
    newstr = newstr.replace("g","h")
    newstr = newstr.replace("l","@d")
    newstr = newstr.replace("o","3")
    newstr = newstr.replace("c","9")
    newstr = newstr.replace("k","d")
    return newstr

def encrypt2(num):
    match num:
        case "1":
            return "ab6546dl"
        case "2":
            return "rgdgfhdf"
        case "3":
            return "ab53gdl"
        case "4":
            return "ab587l"
        case "5":
            return "fg45nf"
        case "6":
            return "th84hdg09jf"
        case "7":
            return "hdfh4sfg68tg"
        case "8":
            return "h54ghsfg58o"
        case "9":
            return "ah566hbdl"
        case "0":
            return "abgdfhd47dl"


def encrypt1(code):
    strCode = str(code)
    code = []
    generatedCode = ""

    for word in strCode:
        code.append(word)

    for i in range(0, len(code)):
        code[i] = encrypt2(code[i])
    
    for items in code:
        generatedCode = generatedCode + items
    
    return encryption3(generatedCode)
    