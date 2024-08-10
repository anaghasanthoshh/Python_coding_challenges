

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]
friendship_pairs = [(0, 1), (0, 2), (1,0),(1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

#1.iterate thru users,capture id and name.
friendship={user["id"]:[] for user in users}
#longer version being
# friendship={}
#for user in users:
# friendship[user["id"]]=[]


print(friendship)
#to loop in through the pairs
for i,j in friendship_pairs:
    friendship[i].append(j)
    friendship[j].append(i)
    #helps in removing duplicates
    friendship[i]=list(dict.fromkeys(friendship[i]))
    friendship[j] = list(dict.fromkeys(friendship[j]))
print(friendship)