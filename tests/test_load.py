import os
import uuid
import pytest
from dundie.core import load
from tests.constants import PEOPLE_FILE

# def setup_module():
#     print("\nisso é executado antes dos testes\n")

# def teardown_module():
#     print("\nisso é executado logo após os testes\n")

# @pytest.fixture(scope="function", autouse=True)  autouse=True aplica para todos testes aqui
@pytest.fixture(scope="function")
def create_a_file(tmpdir):
    file = tmpdir.join("new_file.txt")
    file.write("isso é apenas sujeira...")
    yield
    file.remove()

@pytest.mark.unit
@pytest.mark.high
def test_load_positive_people_list_has_size_2(create_a_file):
    with open(f"arquivo_indesejado_{uuid.uuid4()}.txt", "w") as file_:
        file_.write("dados úteis somente para o teste.....")
    assert len(load(PEOPLE_FILE)) == 2

@pytest.mark.unit
@pytest.mark.high
def test_load_positive_first_person_starts_with_j(request):
    filepath = f"arquivo_indesejado_{uuid.uuid4()}.txt"
    request.addfinalizer(lambda: os.unlink(filepath))
    
    with open(filepath, "w") as file_:
        file_.write("dados úteis somente para o teste.....")

    assert load(PEOPLE_FILE)[0].upper().startswith('J') == True
