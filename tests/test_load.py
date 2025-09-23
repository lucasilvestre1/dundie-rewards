import os
import uuid
import pytest
from dundie.core import load
from tests.constants import PEOPLE_FILE

@pytest.mark.unit
@pytest.mark.high
def test_load_positive_people_list_has_size_2(request):
    """Test function load"""
    assert len(load(PEOPLE_FILE)) == 2


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_first_person_starts_with_j(request):
    """Test function load"""
    assert load(PEOPLE_FILE)[0].upper().startswith('J') == True
