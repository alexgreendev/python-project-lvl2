import os

from gendiff.diff.tree import build_tree
from gendiff.diff.render_stylish import render_stylish
from gendiff.parsers import parse_file


def check_files_extension_match(*files_paths) -> bool:
    unique_extensions = {file_path.split('.')[-1] for file_path in files_paths}
    return len(unique_extensions) == 1


def check_exists_files(*files_paths) -> bool:
    return all(map(os.path.isfile, files_paths))


def generate_diff(
        file_path1: str,
        file_path2: str,
):
    if not check_exists_files(file_path1, file_path2):
        raise FileNotFoundError(
            f'One of or both files is not exists.'
            f' Provided files: {[file_path1, file_path2]}')

    if not check_files_extension_match(file_path1, file_path2):
        raise TypeError(f'Files must be same extensions.'
                        f' Provided files: {[file_path1, file_path2]}')

    with open(file_path1) as file1, open(file_path2) as file2:
        data1 = parse_file(file1)
        data2 = parse_file(file2)

    diff_tree = build_tree(data1, data2)
    return render_stylish(diff_tree)
