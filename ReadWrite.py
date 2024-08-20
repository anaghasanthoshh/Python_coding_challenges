
with open("data.txt") as data:#opening the file
    txt=data.read()#accessing the contents
print(txt)

with open("data.txt",mode="a") as data:
    data.write("\nNew line added")


