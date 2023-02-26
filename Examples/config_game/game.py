from configparser import ConfigParser
import random

config = ConfigParser()
config.read("number_quessing.ini")

user = input("What is your username: ")
if user == "SUDO":
    password = input("Password: ")
    if password != "12345":
        print("Wrong!")
        exit(0)

try:
    config_data = config[user]
except:
    print("User not found!")
    exit(0)


number = random.randint(1, 10 ** (int(config_data['numberdigits'])))
max_tries = int(config_data['numberoftries'])
print(f"{max_tries} -----------------------")
tries = 0
done = False

while not done:
    guess = input("Guess: ")
    if guess == "cheat":
        if "cheats" in config_data.keys() and config_data["cheats"] == "on":
            print(f"You won. The number was {number}!")
            exit(0)
        else:
            print("You are not allowed to cheat!")
            exit(0)
    else:
        guess = int(guess)

    tries += 1

    if guess == number:
        print("fYou won! The number was {number}!")
        print("fIt took you {tries} tries!")
        exit(0)
    else:
        if tries == max_tries:
            print(f"You lost after {tries} tries!")
            print(f"The number was {number} number !")
            exit(0)            
        else:
            if guess > number:
                print("Too high")
            else:
                print("Too low")


