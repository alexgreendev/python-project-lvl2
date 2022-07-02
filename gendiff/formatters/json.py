import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gendiff.tree import DiffTree


def render(
    tree: 'DiffTree',
) -> str:
    return json.dumps(
        tree.__dict__(),
        indent=2,
    )
