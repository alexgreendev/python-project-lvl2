import os

import pytest

FIXTURES_FOLDER = 'fixtures'


@pytest.fixture(scope='function')
async def prepared_files(request):
    file1_name, file2_name, result_file_name = request.param

    fixtures_path = os.path.join(os.path.dirname(__file__), FIXTURES_FOLDER)

    with open(os.path.join(fixtures_path, result_file_name)) as file:
        return (
            os.path.join(fixtures_path, file1_name),
            os.path.join(fixtures_path, file2_name),
            file.read(),
        )
