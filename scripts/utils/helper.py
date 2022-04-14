import json
import os


def dump_to_json(_data: dict, _pathToFile: str, _indent: int = 4):
    """Dump data to *.json file."""
    with open(_pathToFile, "w") as file:
        json.dump(_data, file, indent=_indent)


def load_from_json(_pathToFile: str) -> dict:
    """Return loaded data from *.json file."""
    if os.path.exists(_pathToFile) == False:
        dump_to_json({}, _pathToFile)

    with open(_pathToFile, "r+") as file:
        data = json.load(file)
    return data
