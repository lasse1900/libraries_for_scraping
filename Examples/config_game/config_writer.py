from configparser import ConfigParser

config = ConfigParser()

config["DEFAULT"] = {
    "numberdigits": 6,
    "numberoftries": 8,
    "playername": "Player"
}

config["NeuralNine"] = {
    "numberdigits": 10,
    "numberoftries": 6,
    "playername": "Lasse"
}

config["SUDO"] = {
    "numberdigits": 6,
    "numberoftries": 5,
    "playername": "Cheater",
    "cheats": "on"
}

with open("number_quessing.ini", "w") as f:
    config.write(f)