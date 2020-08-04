#logic gates

def andgate(inputa, inputb):
    if inputa == "0" and inputb == "0":
        aresult = "0"
    elif inputa == "0" and inputb == "1":
        aresult = "0"
    elif inputa == "1" and inputb == "0":
        aresult = "0"
    else:
        aresult = "1"
    return aresult

def notgate(inputa):
    if inputa == "0":
        return 1
    else:
        return 0



gate = input("Enter Logic Gate")

while gate != "q":
    input1 = input("Enter First Input")
    input2 = input("Enter Second Input")

    if gate == "and":
        result = andgate(input1, input2)
    elif gate == "or":
        print("or code")
    elif gate == "xor":
        print("xor code")
    elif gate == "nand":
        result = andgate(input1, input2)
        result = notgate(result)
    else:
        print("not a valid input")



    print("Result = " + str(result))

    gate = input("Enter Logic Gate")
    

