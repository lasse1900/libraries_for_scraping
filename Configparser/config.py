import configparser
import pathlib
from typing import Tuple

# https://www.youtube.com/watch?v=8DOMthoj894


def get_user_pass(section: str = "DEFAULT") -> Tuple[str, str]:
    config_file_path = pathlib.Path(
        __file__).parent.absolute().joinpath("config.ini")
    config = configparser.ConfigParser()
    config.read(config_file_path)

    try:
        data = config[section]
    except KeyError:
        # raise KeyError("Invalid section '{}' specified. Must be one of ['Default'], '{}'".format(section, "', '".join(config.sections())))
        raise KeyError(f"""Invalid section '{section}' specified. Must be one of ['Default'], '{"', '".join(config.sections())}']""")

    return data["username"], data["password"]


print(get_user_pass("DEFAULT"))
