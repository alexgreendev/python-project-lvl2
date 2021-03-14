from typing import TYPE_CHECKING

from .json_parse import json_parse
from .yml_parse import yml_parse
from .cmd_args import parse_cmd_args

if TYPE_CHECKING:
    from typing import Dict, Any
    from typing.io import TextIO


def get_file_format(file: 'TextIO') -> str:
    return file.name.split('.')[-1]


def parse_file(file: 'TextIO') -> 'Dict[str, Any]':
    file_format = get_file_format(file)

    if file_format == 'json':
        return json_parse(file)
    elif file_format in ('yml', 'yaml'):
        return yml_parse(file)

    raise TypeError(f'Unknown file format: {file_format}')
