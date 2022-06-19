from gendiff.formatters.render_stylish import render_stylish

from gendiff.tree import DiffTree


def format_data(format_name: str, tree: DiffTree) -> str:
    if format_name == 'stylish':
        return render_stylish(tree)

    raise ValueError(f'Unknown format: {format_name}')

