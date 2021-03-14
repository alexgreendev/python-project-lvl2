from typing import TYPE_CHECKING

import yaml


if TYPE_CHECKING:
    from typing import Dict, Any
    from typing.io import TextIO


def yml_parse(file: 'TextIO') -> 'Dict[str, Any]':
    test = yaml.safe_load(file)
    return test
