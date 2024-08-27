import pandas as pd
df=pd.read_csv("nato_phonetic_alphabet.csv")
#print(df)

#for  index,row in df.iterrows():
#    print(row["letter"])


data={row["letter"]:row["code"] for  index,row in df.iterrows() }
#print(data)
word=str(input("Type the word!"))
split_word=list(word)
NATO=[]
for letter in word:
    NATO.append(data[letter])
print(NATO)




