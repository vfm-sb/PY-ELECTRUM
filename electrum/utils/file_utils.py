# Built-in Modules
from pathlib import Path
import json


def get_root_path() -> Path | None:
    marker_filename = "pyproject.toml"
    current_directory = Path.cwd()
    home_directory = Path.home()
    while current_directory != home_directory:
        marker_file = current_directory / marker_filename
        if marker_file.is_file():
            return current_directory
        current_directory = current_directory.parent
    return None


def get_folder_path(path: str) -> Path | None:
    root_path = get_root_path()
    if root_path is None:
        return None
    return root_path / path


def get_file_path(filename: str, path: str) -> Path | None:
    folder_path = get_folder_path(path)
    if folder_path is None:
        return None
    return str(folder_path / filename)


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


# Testing
if __name__ == "__main__":
    pass
