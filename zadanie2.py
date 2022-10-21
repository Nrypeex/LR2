def zad2():
    doFor2 = []
    doFor3 = []
    doFor5 = []
    intList = []

    print("input >0 nums")
    print("to end input '0'")

    while 1:
        inputInteger = int(input())
        if inputInteger == 0:
            break
        intList.append(inputInteger)
    for i in range(len(intList)) :
        if(intList[i] % 2 == 0): doFor2.append(intList[i])
        if(intList[i] % 3 == 0): doFor3.append(intList[i])
        if(intList[i] % 5 == 0): doFor5.append(intList[i])
    print(doFor2)
    print(doFor3)
    print(doFor4)


            
        
    
    print(intList)