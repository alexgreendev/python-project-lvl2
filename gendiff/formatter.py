from enum import Enum

from gendiff.formatters import stylish, plain

from gendiff.tree import DiffTree


class FormatNameEnum(str, Enum):
    stylish = 'stylish'
    plain = 'plain'


def format_data(format_name: str, tree: DiffTree) -> str:
    if format_name == FormatNameEnum.stylish:
        return stylish.render(tree)

    elif format_name == FormatNameEnum.plain:
        return plain.render(tree)

    raise ValueError(f'Unknown format: {format_name}')
