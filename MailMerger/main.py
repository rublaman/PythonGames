invites_names_path = "./Input/Names/invited_names.txt"
starting_letter_path = "./Input/Letters/starting_letter.txt"


with open(starting_letter_path, "r") as starting_letter:
    letter = starting_letter.read()

    with open(invites_names_path, "r") as invited_names:
        for name in invited_names.readlines():
            correct_name = name.rstrip('\n')
            letter = letter.replace("[name]", correct_name)
            print(correct_name)

            with open(f"./Output/ReadyToSend/{correct_name}.txt", "w") as new_letter:
                new_letter.write(letter)
