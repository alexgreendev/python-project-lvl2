import pytest
from gendiff import generate_diff, FormatNameEnum


@pytest.mark.asyncio
@pytest.mark.parametrize(
    argnames='prepared_files',
    argvalues=[
        [
            'file1.json',
            'file2.json',
            'stylish',
        ],
        [
            'file1.yml',
            'file2.yml',
            'stylish',
        ],
        [
            'file1_nested.yml',
            'file2_nested.yml',
            'stylish_nested',
        ],
    ],
    indirect=True,
)
async def test_stylish(
    prepared_files,
):
    file1_path, file2_path, result_render = prepared_files

    assert result_render == generate_diff(
        file1_path,
        file2_path,
    )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    argnames='prepared_files',
    argvalues=[
        [
            'file1.json',
            'file2.json',
            'plain',
        ],
        [
            'file1.yml',
            'file2.yml',
            'plain',
        ],
        [
            'file1_nested.yml',
            'file2_nested.yml',
            'plain_nested',
        ],
    ],
    indirect=True,
)
async def test_plain(
    prepared_files,
):
    file1_path, file2_path, result_render = prepared_files

    assert result_render == generate_diff(
        file1_path,
        file2_path,
        FormatNameEnum.plain,
    )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    argnames='prepared_files',
    argvalues=[
        [
            'file1_nested.yml',
            'file2_nested.yml',
            'json_nested',
        ],
    ],
    indirect=True,
)
async def test_json(
    prepared_files,
):
    file1_path, file2_path, result_render = prepared_files

    assert result_render == generate_diff(
        file1_path,
        file2_path,
        FormatNameEnum.json,
    )
