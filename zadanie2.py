def zad2():
    intList = []

    print("input >0 nums")
    print("to end input '0'")

    while 1:
        inputInteger = int(input())
        if inputInteger == 0:
            break
        intList.append(inputInteger)
    
    print(intList)