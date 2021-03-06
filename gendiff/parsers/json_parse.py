import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Dict, Any
    from typing.io import TextIO


def json_parse(file: 'TextIO') -> 'Dict[str, Any]':
    return json.load(file)
