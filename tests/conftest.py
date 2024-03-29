import os

import pytest


@pytest.fixture(scope='function')
async def prepared_files(request):
    file1_name, file2_name, result_file_name = request.param

    fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')

    with open(os.path.join(fixtures_path, result_file_name)) as result_file:
        return (
            os.path.join(fixtures_path, file1_name),
            os.path.join(fixtures_path, file2_name),
            result_file.read(),
        )
