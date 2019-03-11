import pytest
from responses import RequestsMock


@pytest.fixture()
def mock_requests():
    with RequestsMock() as reqs:
        yield reqs
