import pytest
from dundie.core import load
from tests.constants import PEOPLE_FILE

@pytest.mark.unit
def test_load():
    assert load(PEOPLE_FILE)[0].startswith('Jim') == True
    assert len(load(PEOPLE_FILE)) == 2
