a = 0
a = int(input())
b = a
numList = []
numList2 = []

while b > 0:
    print(b)
    numList.append(int(a%10))
    a=a/10
    b = int(b/10)
print(numList)
c = 1
numList2 = numList.copy()
numList2.reverse()
print(numList2)
for i in range(len(numList)):
    if numList[i] != numList2[i]:
        c = 0
if c:
    print("polyndrome")
else:
    print("not polyndrome")
