from enum import Enum
from typing import Dict, Any, List, Union


class DiffNodeTypeEnum(str, Enum):
    root = 'root'
    unchanged = 'unchanged'
    changed = 'changed'
    inserted = 'inserted'
    deleted = 'deleted'
    nested = 'nested'


class DiffTree:
    def __init__(
        self,
        type_node: DiffNodeTypeEnum,
        key: str = None,
        value: Union[str, int, bool] = None,
        value1: Union[str, int, bool] = None,
        value2: Union[str, int, bool] = None,
        children: List['DiffTree'] = None,
    ):

        self.type_node = type_node
        self.key = key
        self.value = value
        self.value1 = value1
        self.value2 = value2
        self.children = children or []

    def __dict__(self):
        if self.type_node == DiffNodeTypeEnum.root:
            return dict(
                type=self.type_node,
                children=list(
                    map(lambda child: child.__dict__(), self.children)),
            )
        elif self.type_node == DiffNodeTypeEnum.nested:
            return dict(
                type=self.type_node,
                key=self.key,
                children=list(
                    map(lambda child: child.__dict__(), self.children)),
            )
        elif self.type_node == DiffNodeTypeEnum.inserted:
            return dict(
                type=self.type_node,
                key=self.key,
                value=self.value,
            )
        elif self.type_node == DiffNodeTypeEnum.deleted:
            return dict(
                type=self.type_node,
                key=self.key,
                value=self.value,
            )
        elif self.type_node == DiffNodeTypeEnum.changed:
            return dict(
                type=self.type_node,
                key=self.key,
                value1=self.value1,
                value2=self.value2,
            )
        elif self.type_node == DiffNodeTypeEnum.unchanged:
            return dict(
                type=self.type_node,
                key=self.key,
                value=self.value,
            )


def build_nodes(
        data1: Dict[str, Any],
        data2: Dict[str, Any]
) -> List[DiffTree]:
    nodes = []

    keys = data1.keys() | data2.keys()

    for key in sorted(keys):
        if key not in data2:
            nodes.append(DiffTree(
                type_node=DiffNodeTypeEnum.deleted,
                key=key,
                value=data1[key],
            ))
        elif key not in data1:
            nodes.append(DiffTree(
                type_node=DiffNodeTypeEnum.inserted,
                key=key,
                value=data2[key],
            ))
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            nodes.append(DiffTree(
                type_node=DiffNodeTypeEnum.nested,
                key=key,
                children=build_nodes(data1[key], data2[key]),
            ))
        elif data1[key] != data2[key]:
            nodes.append(DiffTree(
                type_node=DiffNodeTypeEnum.changed,
                key=key,
                value1=data1[key],
                value2=data2[key],
            ))
        else:
            nodes.append(DiffTree(
                type_node=DiffNodeTypeEnum.unchanged,
                key=key,
                value=data1[key],
            ))

    return nodes


def build(
    data1: Dict[str, Any],
    data2: Dict[str, Any]
) -> DiffTree:
    return DiffTree(
        type_node=DiffNodeTypeEnum.root,
        children=build_nodes(data1, data2),
    )
