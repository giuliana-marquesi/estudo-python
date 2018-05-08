def incomodam(n):
    if n < 1:
        return ""
    return "incomodam " + incomodam(n -1)
    
def elefantes(n):
    if n < 1:
        return ""
    if n == 1:
        return "Um elefante incomoda muita gente\n"
    
    return elefantes(n -1) + str(n) + " elefantes " + incomodam(n) + "muito mais\n" + str(n) + " elefantes incomodam muita gente\n"
