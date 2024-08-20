"""
2.	Matrix Transposition:
	•	Given a 2D matrix (list of lists), transpose it using list comprehension.
	•	Example: [[1, 2, 3], [4, 5, 6]] → [[1, 4], [2, 5], [3, 6]]

"""
import numpy as np
matrix=[[1, 2, 3,7], [4, 5, 6,8],[9,10,11,12]]
reversed=[[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(reversed)

