import os
from typing import Dict

from gendiff.formatter import format_data
from gendiff.parser import parse
from gendiff import tree


def check_files_extension_match(*files_paths) -> bool:
    unique_extensions = {file_path.split('.')[-1] for file_path in files_paths}
    return len(unique_extensions) == 1


def check_exists_files(*files_paths) -> bool:
    return all(map(os.path.isfile, files_paths))


def get_file_format(file_path: str) -> str:
    _, extension = os.path.splitext(file_path)
    return extension.lower()[1:]


def get_data(file_path: str) -> Dict:
    with open(file_path) as data:
        return parse(data, get_file_format(file_path))


def generate_diff(
        file_path1: str,
        file_path2: str,
        format_name='stylish',
) -> str:
    if not check_exists_files(file_path1, file_path2):
        raise FileNotFoundError(
            f'One of or both files is not exists.'
            f' Provided files: {[file_path1, file_path2]}')

    if not check_files_extension_match(file_path1, file_path2):
        raise TypeError(f'Files must be same extensions.'
                        f' Provided files: {[file_path1, file_path2]}')

    data1 = get_data(file_path1)
    data2 = get_data(file_path2)

    diff_tree = tree.build(data1, data2)
    return format_data(format_name, diff_tree)
