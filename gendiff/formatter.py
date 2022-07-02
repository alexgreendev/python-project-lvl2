from enum import Enum

from gendiff.formatters import stylish, plain, json

from gendiff.tree import DiffTree


class FormatNameEnum(str, Enum):
    stylish = 'stylish'
    plain = 'plain'
    json = 'json'


def format_data(format_name: str, tree: DiffTree) -> str:
    if format_name == FormatNameEnum.stylish:
        return stylish.render(tree)

    elif format_name == FormatNameEnum.plain:
        return plain.render(tree)

    elif format_name == FormatNameEnum.json:
        return json.render(tree)

    raise ValueError(f'Unknown format: {format_name}')
