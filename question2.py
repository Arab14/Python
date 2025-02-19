def calculateAInverse(matrix, firstNum, secondNum):
    d = (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
    
    if (d == 0):
        print("NO UNIQUE SOLUTION")
        return False
    
    inverseMatrix = [
        [matrix[1][1]/d, -matrix[0][1]/d],
        [-matrix[1][0]/d, matrix[0][0]/d]
    ]
    
    b = [firstEquation[2], secondEquation[2]]
    x, y = (inverseMatrix[0][0]*b[0] + inverseMatrix[0][1]*b[1]), (inverseMatrix[1][0]*b[0] + inverseMatrix[1][1]*b[1])
    
    return x, y 


firstEquation = [2, 2, 5]
secondEquation = [3, 4, 6]

matrix = [
    [1, 2],
    [3, 5]
]

x, y = calculateAInverse(matrix, firstEquation, secondEquation)
print(f"X is: {x} \nY is {y}")
