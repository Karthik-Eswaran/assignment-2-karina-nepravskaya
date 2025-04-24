import importlib
from pathlib import Path

def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_file(file_path: str, content: str) -> None:
    with open(file_path, 'w') as file:
        file.write(content)


def list_files_in_directory(directory_path: str) -> list:
    dir_path = Path(directory_path)
    return [item.name for item in dir_path.iterdir() if item.is_file()]


def generate_numbers(n: int) -> iter:
    return [i for i in range(n)]


def use_function_from_module(module_name: str, function_name: str, *args) -> any:
    module = importlib.import_module(module_name)
    function = getattr(module, function_name)
    return function(*args)