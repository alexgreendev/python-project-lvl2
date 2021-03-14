import os

import pytest

FIXTURES_FOLDER = 'fixtures'


@pytest.fixture(scope='function')
async def result_render(request):
    assert getattr(request.module, 'FORMATTER', None)

    result_path = os.path.join(
        os.path.dirname(__file__), FIXTURES_FOLDER, request.module.FORMATTER)

    with open(result_path) as file:
        return file.read()
