import configparser
import pathlib

from typing import Tuple
# https://www.youtube.com/watch?v=8DOMthoj894

config = configparser.ConfigParser()
config.read("config.ini")

# print(config)
# print(config.sections())

# print(config["DEFAULT"]["USERNAME"])
# print(config["DEFAULT"]["password"])

def get_user_pass(section: str = "DEFAULT") -> Tuple[str,str]:
    config_file_path = pathlib.Path(__file__).parent.absolute().joinpath("config.ini")
    config.read(config_file_path)

    return config[section]["username"], config[section]["password"]

print(get_user_pass("Github"))