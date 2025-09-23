import pytest
from subprocess import check_output

@pytest.mark.integration
def test_load():
    """tests load command"""
    result = check_output(
        ["dundie", "load", "tests/assets/people.csv"]
    ).decode("utf-8").strip().split('\n\n')
    assert len(result) == 3
