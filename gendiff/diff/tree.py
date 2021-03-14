from enum import Enum
from typing import Dict, Any, NamedTuple, List, Union


class DiffNodeTypeEnum(str, Enum):
    root = 'root'
    unchanged = 'unchanged'
    changed = 'changed'
    inserted = 'inserted'
    deleted = 'deleted'


class DiffTree(NamedTuple):
    type: DiffNodeTypeEnum
    key: str = None
    value: Union[str, int, bool] = None
    value1: Union[str, int, bool] = None
    value2: Union[str, int, bool] = None
    children: List['DiffTree'] = []


def build_tree(
        data1: Dict[str, Any],
        data2: Dict[str, Any]
) -> DiffTree:
    nodes = []

    all_keys = [*data2.keys(), *data1.keys()]
    unique_keys = {key: None for key in all_keys}.keys()

    node_type, key, value, value1, value2 = (None,) * 5
    for index, key in enumerate(unique_keys):
        if key not in data2:
            node_type = DiffNodeTypeEnum.deleted
            key = key
            value = data1[key]
        elif key not in data1:
            node_type = DiffNodeTypeEnum.inserted
            key = key
            value = data2[key]
        elif data1[key] != data2[key]:
            node_type = DiffNodeTypeEnum.changed
            key = key
            value1 = data1[key]
            value2 = data2[key]
        else:
            node_type = DiffNodeTypeEnum.unchanged
            key = key
            value = data1[key]

        nodes.append(DiffTree(
            type=node_type,
            key=key,
            value=value,
            value1=value1,
            value2=value2,
            children=[],
        ))

    return DiffTree(
        type=DiffNodeTypeEnum.root,
        children=nodes,
    )
