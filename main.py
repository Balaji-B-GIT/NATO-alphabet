import pandas
names_data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_names = {row.letter:row.code for (index, row) in names_data.iterrows()}
while True:
    try:
        user_name = input("Enter your name:").upper()
        nato_alpha = [dict_names[key] for key in user_name]
    except KeyError:
        print("enter alphabets")
    else:
        print(nato_alpha)
        break
