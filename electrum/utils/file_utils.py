# Built-in Modules
import os
import json


def get_root_path() -> str:
    current_script_path = os.path.abspath(__file__)
    utils_path = os.path.dirname(current_script_path)
    project_path = os.path.dirname(utils_path)
    project_root = os.path.dirname(project_path)
    return project_root


def get_folder_path(path: str) -> str:
    return get_root_path() + "/" + path + "/"


def get_file_path(filename: str, path: str) -> str:
    return get_folder_path(path) + filename


def get_file_content(filename: str, path: str) -> str:
    filepath = get_file_path(filename, path)
    with open(filepath, "r", encoding="UTF-8") as file:
        return file.read()


def save_file_content(filename: str, path: str, content: str) -> None:
    filepath = get_file_path(filename, path)
    with open(filepath, "w", encoding="UTF-8") as file:
        file.write(content)


def get_json_file(filename: str, path: str) -> dict:
    if not filename.endswith(".json"):
        raise ValueError("Invalid JSON Filename")
    file_content = get_file_content(filename, path)
    return json.loads(file_content)


def save_json_file(filename: str, path: str, data: dict) -> None:
    if not filename.endswith(".json"):
        raise ValueError("Invalid JSON Filename")
    json_string = json.dumps(data, indent=4)
    save_file_content(filename, path, json_string)
