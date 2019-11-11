import json

while True:
    with open('birthdays.json', 'w') as f:
        name = input("Please enter the name of a person: ")
        birthday = input("Please enter the birthday of the person: ")

        data = {
            "name": name,
            "birthday": birthday
        }

        json.dump(data, f)
        break
