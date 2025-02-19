from copy import deepcopy
import numpy as np

A = [
    [1, 2, -1],
    [-2, 2, 3],
    [2, 4, 4]
]
B = [6, 3, 4]

AB = deepcopy(A)
for i in range(len(A)):
    AB[i].append(B[i])

rankA = np.linalg.matrix_rank(A)
rankAB = np.linalg.matrix_rank(AB)
numVar = len(A[0])

print(f"Rank of [ A ]: {rankA} \nRank of [A | B]: {rankAB} \nNumVar: {numVar}")

if rankA == rankAB:
    if rankA == numVar:
        print("System is consistent with a unique Solution.")
    else:
        print("System is consistent with a infinity Solution.")
else:
    print("System is inconsistent.")