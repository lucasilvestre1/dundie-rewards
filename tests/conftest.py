MARKER = """\
unit: Mark unit tests
integration: Mark integration tests
high: Mark High Priority tests
medium: Mark Medium Priority tests
low: Mark Low Priority tests 
"""

def pytest_configure(config):
    map(lambda line: config.addinivalue_line("markers", line), MARKER.split("\n"))
