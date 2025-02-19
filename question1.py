def calculateLinear(firstNum, secondNum):
    d = (firstNum[0]*secondNum[1])-(secondNum[0]*firstNum[1])
    d1 = (firstNum[2]*secondNum[1])-(secondNum[2]*firstNum[1])
    d2 = (firstNum[0]*secondNum[2])-(secondNum[0]*firstNum[2])
    
    return d, d1, d2

firstEquation = [1, 1, 3]
secondEquation = [1, -1, 1]

d, d1, d2 = calculateLinear(firstEquation, secondEquation)

if (d==0 and d1!=0 and d2!=0):
    print("No Solution")
elif (d==0 and d1==0 and d2==0):
    print("Infinite Solution")
else:
    x = d1/d
    y = d2/d
    print(f"\nX is: {x} \nY is: {y}\n")