from enum import Enum
from typing import Dict, Any, NamedTuple, List, Union


class DiffNodeTypeEnum(str, Enum):
    root = 'root'
    unchanged = 'unchanged'
    changed = 'changed'
    inserted = 'inserted'
    deleted = 'deleted'
    nested = 'nested'


class DiffTree(NamedTuple):
    type: DiffNodeTypeEnum
    key: str = None
    value: Union[str, int, bool] = None
    value1: Union[str, int, bool] = None
    value2: Union[str, int, bool] = None
    children: List['DiffTree'] = []


def build_nodes(
        data1: Dict[str, Any],
        data2: Dict[str, Any]
) -> List[DiffTree]:
    nodes = []

    keys = data1.keys() | data2.keys()

    for key in sorted(keys):
        if key not in data2:
            nodes.append(DiffTree(
                type=DiffNodeTypeEnum.deleted,
                key=key,
                value=data1[key],
            ))
        elif key not in data1:
            nodes.append(DiffTree(
                type=DiffNodeTypeEnum.inserted,
                key=key,
                value=data2[key],
            ))
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            nodes.append(DiffTree(
                type=DiffNodeTypeEnum.nested,
                key=key,
                children=build_nodes(data1[key], data2[key]),
            ))
        elif data1[key] != data2[key]:
            nodes.append(DiffTree(
                type=DiffNodeTypeEnum.changed,
                key=key,
                value1=data1[key],
                value2=data2[key],
            ))
        else:
            nodes.append(DiffTree(
                type=DiffNodeTypeEnum.unchanged,
                key=key,
                value=data1[key],
            ))

    return nodes


def build(
    data1: Dict[str, Any],
    data2: Dict[str, Any]
) -> DiffTree:
    return DiffTree(
        type=DiffNodeTypeEnum.root,
        children=build_nodes(data1, data2),
    )
