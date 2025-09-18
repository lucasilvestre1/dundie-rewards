import pytest

MARKER = """\
unit: Mark unit tests
integration: Mark integration tests
high: Mark High Priority tests
medium: Mark Medium Priority tests
low: Mark Low Priority tests 
"""

def pytest_configure(config):
    map(lambda line: config.addinivalue_line("markers", line), MARKER.split("\n"))


@pytest.fixture(autouse=True)
def go_to_tmpdir(request):
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield
