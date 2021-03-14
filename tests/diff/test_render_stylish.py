import pytest
from gendiff import generate_diff

FORMATTER = 'stylish'


@pytest.mark.asyncio
async def test_json(file1_json_path, file2_json_path, result_render):
    assert result_render == generate_diff(file1_json_path, file2_json_path)
