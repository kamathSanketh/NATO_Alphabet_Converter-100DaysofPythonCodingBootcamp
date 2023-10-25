import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
letter = data["letter"]
code = data["code"]
dict = {}
for x in range(0, len(letter)):
    dict[letter[x]] = code[x]
temp = input()
userInput = [x for x in temp]
result = []
for letter in userInput:
    result.append(dict[letter])
print(result)
