from typing import Optional, Union, TYPE_CHECKING, Dict
from gendiff.tree import DiffNodeTypeEnum

if TYPE_CHECKING:
    from gendiff.tree import DiffTree


def _value_to_str(
    data: Optional[Union[str, int, bool, Dict]],
) -> str:
    if isinstance(data, bool):
        return 'true' if data else 'false'

    if data is None:
        return 'null'

    if isinstance(data, str):
        return f"'{data}'"

    if isinstance(data, dict) or isinstance(data, list):
        return "[complex value]"

    return str(data)


def _node_processing(
    node: 'DiffTree',
    parent_path: str = '',
) -> Optional[str]:
    property_path = f"{parent_path}{node.key}"

    children = node.children
    value = _value_to_str(node.value)
    value1 = _value_to_str(node.value1)
    value2 = _value_to_str(node.value2)

    if node.type == DiffNodeTypeEnum.root:
        lines = map(
            lambda child: _node_processing(child),
            children,
        )
        return '\n'.join(filter(bool, lines))

    elif node.type == DiffNodeTypeEnum.nested:
        lines = map(
            lambda child: _node_processing(child, f"{property_path}."),
            children,
        )
        return '\n'.join(filter(bool, lines))

    elif node.type == DiffNodeTypeEnum.inserted:
        return f"Property '{property_path}'" \
               f" was added with value: {value}"

    elif node.type == DiffNodeTypeEnum.deleted:
        return f"Property '{property_path}' was removed"

    elif node.type == DiffNodeTypeEnum.changed:
        return f"Property '{property_path}' was updated." \
               f" From {value1} to {value2}"

    elif node.type == DiffNodeTypeEnum.unchanged:
        return

    raise ValueError(f"Unknown type: {node.type}")


def render(tree: 'DiffTree') -> str:
    return _node_processing(tree)
