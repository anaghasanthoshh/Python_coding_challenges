"""
1.	Nested List Flattening with Condition:
	•	Given a list of lists, flatten it and only include numbers that are even.
	•	Example: [[1, 2, 3], [4, 5, 6], [7, 8, 9]] → [2, 4, 6, 8]
"""
test=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#flat_result=[num for num in row   for row in test]
flat=[]
#for row in test:
#     for num in row:
#        flat.append(num)

flat=[num for row in test for num in row if num%2==0]
print(flat)





#flat_result=[num for sublist in test for num in sublist if num%2==0]
#loops through outer loop to get sublists and then loops into sublist to get the numbers
#print(flat_result)
