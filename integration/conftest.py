MARKER = """\
unit: Mark unit tests
integration: Mark integration tests
high: Mark High Priority tests
medium: Mark Medium Priority tests
low: Mark Low Priority tests 
"""

def pytest_configure(config):
    for line in MARKER.split("\n"):
        config.addinivalue_line("markers", line)
