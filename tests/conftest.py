import asyncio
import os

import pytest

FIXTURES_FOLDER = 'fixtures'


@pytest.fixture(scope='module')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
def file1_json_path():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'file1.json')


@pytest.fixture(scope='session')
def file2_json_path():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'file2.json')


@pytest.fixture(scope='session')
def file1_yml_path():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'file1.yml')


@pytest.fixture(scope='session')
def file2_yml_path():
    return os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'file2.yml')
