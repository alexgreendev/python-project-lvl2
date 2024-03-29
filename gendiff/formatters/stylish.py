from typing import Optional, Union, TYPE_CHECKING, Dict
from gendiff.tree import DiffNodeTypeEnum

if TYPE_CHECKING:
    from gendiff.tree import DiffTree


def build_indent(depth: int) -> str:
    return ' ' * (depth * 4 - 2)


def _value_to_str(
    data: Optional[Union[str, int, bool, Dict]],
    depth: int,
) -> str:
    if isinstance(data, bool):
        return 'true' if data else 'false'

    if data is None:
        return 'null'

    if isinstance(data, dict):
        parts = []
        for key in data:
            indent = build_indent(depth + 1)
            formatted_value = _value_to_str(data[key], depth + 1)
            parts.append(f"{indent}  {key}: {formatted_value}")
        output = '\n'.join(parts)
        return f"{{\n{output}\n{build_indent(depth)}  }}"

    return str(data)


def _node_processing(
    node: 'DiffTree',
    depth: int = 0,
) -> str:
    children = node.children
    value = _value_to_str(node.value, depth)
    value1 = _value_to_str(node.value1, depth)
    value2 = _value_to_str(node.value2, depth)

    indent = build_indent(depth)

    if node.type_node == DiffNodeTypeEnum.root:
        lines = map(lambda child: _node_processing(child, depth + 1), children)
        result = '\n'.join(lines)
        return f'{{\n{result}\n}}'

    elif node.type_node == DiffNodeTypeEnum.nested:
        lines = map(lambda child: _node_processing(child, depth + 1), children)
        result = '\n'.join(lines)
        return f"{indent}  {node.key}: {{\n{result}\n{indent}  }}"

    elif node.type_node == DiffNodeTypeEnum.inserted:
        return f"{indent}+ {node.key}: {value}"

    elif node.type_node == DiffNodeTypeEnum.deleted:
        return f"{indent}- {node.key}: {value}"

    elif node.type_node == DiffNodeTypeEnum.changed:
        lines = [
            f"{indent}- {node.key}: {value1}",
            f"{indent}+ {node.key}: {value2}"
        ]
        return '\n'.join(lines)

    elif node.type_node == DiffNodeTypeEnum.unchanged:
        return f"{indent}  {node.key}: {value}"

    raise ValueError(f"Unknown type: {node.type_node}")


def render(tree: 'DiffTree') -> str:
    return _node_processing(tree)
