import pytest
import requests
from constants import BASE_URL, AUTHOR_NOT_EXIST
from testdata import testdata_poets_lines, testsearch
from helpers import get_real_lines_count


@pytest.mark.parametrize("author_name, lines, poems", testdata_poets_lines)
def test_author_linecount(author_name, lines, poems):
    response = requests.get(f'{BASE_URL}author,linecount/{author_name};{lines}')
    response_json = response.json()
    assert response.status_code == 200
    assert len(response_json) == poems
    for poem in response_json:
        assert get_real_lines_count(poem['lines']) == int(poem['linecount'])


def test_author_not_exist():
    response = requests.get(f'{BASE_URL}author/{AUTHOR_NOT_EXIST}')
    assert response.status_code == 200
    assert response.json() == {"status":404,"reason":"Not found"}


@pytest.mark.parametrize("search", testsearch)
def test_search_by_partial_name(search):
    response = requests.get(f'{BASE_URL}author/{search}')
    response_json = response.json()
    assert response.status_code == 200
    for poem in response_json:
        assert search.lower() in poem["author"].lower()
    authors_set = {poem["author"] for poem in response_json}
    assert len(authors_set) > 1


