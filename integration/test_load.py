import pytest
from subprocess import check_output, CalledProcessError

@pytest.mark.integration
@pytest.mark.medium
def test_load_positive_call_load_command():
    """tests load command"""
    result = check_output(
        ["dundie", "load", "tests/assets/people.csv"]
    ).decode("utf-8").strip().split('\n\n')
    assert len(result) == 3


@pytest.mark.integration
@pytest.mark.medium
@pytest.mark.parametrize("wrong_command", ["loady", "put", "get", "start"])
def test_load_negative_call_load_command_with_wrong_params(wrong_command):
    """tests load command"""
    with pytest.raises(CalledProcessError) as error:
        result = check_output(
            ["dundie", wrong_command, "tests/assets/people.csv"]
        ).decode("utf-8").strip().split('\n\n')
    
    assert "status 2" in str(error.getrepr())
