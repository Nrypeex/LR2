def NRoot ():
    print("input digit")
    A = int(input())
    print("input power")
    pow = int(input())
    result = 1

    while result ** pow < A:
        result = (1/pow)*((pow-1)*result + (A/(result**(pow-1))))
    print(result)