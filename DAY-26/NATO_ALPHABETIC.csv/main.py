import pandas

data = pandas.read_csv(
    "/home/jibril/Documents/Python/DAY-26/NATO_ALPHABETIC/nato_alphabetic.csv"
)
# print(data)
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)
word = input("Enter a Word: ").upper()
word_dict = [phonetic_dict[letter] for letter in word]
print(word_dict)
