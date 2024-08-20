'''1.	Invert a Dictionary:
	•	Given a dictionary, invert it so that the keys become values and values become keys. Assume all values are unique.
	•	Example: {'a': 1, 'b': 2, 'c': 3} → {1: 'a', 2: 'b', 3: 'c'}'''

dic={'a': 1, 'b': 2, 'c': 3}
inv_dic={ value:key for (key,value) in dic.items()}
print(inv_dic)

'''
2.	Filter Dictionary by Key or Value:
	•	Create a new dictionary from an existing one, keeping only the items where the value is greater than a certain threshold.
	•	Example: {'a': 1, 'b': 10, 'c': 15} (with threshold 10) → {'b': 10, 'c': 15}
	
'''
old={'a': 1, 'b': 10, 'c': 15}
new={key:value for (key,value) in old.items() if value>=10 }
print(new)

'''
3.	Merging Two Dictionaries with Value Summation:
	•	Given two dictionaries with the same keys, merge them into a single dictionary by
	    summing the values for each key.
	•	Example: {'a': 1, 'b': 2} and {'a': 3, 'b': 4} → {'a': 4, 'b': 6}
'''
list1={'a': 1, 'b': 2}
list2={'a': 3, 'b': 4}
x=list1.get('a',0)
print(x)
combined={key:list1.get(key,0)+list2.get(key,0) for key in list1}
print(combined)

'''
4.	Group by Frequency:
	•	Given a list of items, create a dictionary where the keys are the
	 items and the values are the frequency of those items.
	•	Example: ['apple', 'banana', 'apple', 'orange'] → 
	{'apple': 2, 'banana': 1, 'orange': 1}
'''
item_list=['apple', 'banana', 'apple', 'orange']
item_dic={fruit:item_list.count(fruit) for fruit in item_list}
print(item_dic)

'''
5.	Dictionary of Lists Filtering:
	•	Given a dictionary where the values are lists, create a new dictionary where
	 each list has been filtered to include only numbers greater than n.
	•	Example: {'a': [1, 5, 3], 'b': [10, 2], 'c': [4, 5]} (with n=3)
	 → {'a': [5], 'b': [10], 'c': [4, 5]}
'''
item_diction={'a': [1, 5, 3], 'b': [10, 2], 'c': [4, 5]}
new_diction={key:[item for item in value if item>3] for (key,value) in item_diction.items() }
print(new_diction)
#if you want to have list as output, the for loop should be inside the list.Remember.
