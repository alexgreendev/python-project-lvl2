from typing import Optional, Union, TYPE_CHECKING
from gendiff.tree import DiffNodeTypeEnum

if TYPE_CHECKING:
    from gendiff.tree import DiffTree


def _value_to_str(data: Optional[Union[str, int, bool]]):
    if isinstance(data, bool):
        return 'true' if data else 'false'

    if data is None:
        return 'null'

    return data


def _node_processing(node: 'DiffTree'):
    children = node.children
    value = _value_to_str(node.value)
    value1 = _value_to_str(node.value1)
    value2 = _value_to_str(node.value2)

    if children:
        lines = map(lambda child: _node_processing(child), children)
        result = '\n'.join(lines)
        return f'{{\n{result}\n}}'

    if node.type == DiffNodeTypeEnum.inserted:
        return f"+ {node.key}: {value}"

    if node.type == DiffNodeTypeEnum.deleted:
        return f"- {node.key}: {value}"

    if node.type == DiffNodeTypeEnum.changed:
        lines = [
            f"- {node.key}: {value1}",
            f"+ {node.key}: {value2}"
        ]
        return '\n'.join(lines)

    if node.type == DiffNodeTypeEnum.unchanged:
        return f"  {node.key}: {value}"


def render_stylish(tree: 'DiffTree') -> str:
    return _node_processing(tree)
