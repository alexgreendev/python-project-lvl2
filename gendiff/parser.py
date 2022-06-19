import json
import yaml

from typing import Dict, Any, TextIO


def parse(data: TextIO, format_name: str) -> Dict[str, Any]:
    if format_name == 'json':
        return json.load(data)
    if format_name in {'yml', 'yaml'}:
        return yaml.safe_load(data)

    raise TypeError(f'Unknown file format: {format_name}')
