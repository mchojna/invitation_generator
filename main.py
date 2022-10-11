with open("./Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

with open("./Input/Names/invited_names.txt") as file:
    names = file.read().split()

for name in names:
    letter = starting_letter.replace("[name]", name)

    with open(f"./Output/ReadyToSend/invitation_{name}_1", mode="w") as file:
        file.write(letter)