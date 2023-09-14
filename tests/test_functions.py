import pytest
from src.data_base_manager import DBManager
from src.request_manager import RequestManager
from src.utils import config, prepare_problem_format
import requests


def test_prepare_problem_format():
    data = {
        'contestId': 1872,
        'index': 'G',
        'name': 'Replace With Product',
        'type': 'PROGRAMMING',
        'tags': ['brute force', 'greedy', 'math'],
        'solvedCount': 2270
    }
    expected = ['1872G', 'Replace With Product', None, None, 2270, 'brute force greedy math']
    assert prepare_problem_format(data) == expected


def test_configuration():
    with pytest.raises(Exception) as info:
        connection_params = config(section="test")
        data_base = DBManager(connection_params, "codeforces_base")
    assert str(info.value) == 'Section test did not find in configuration file.'


def test_confi():
    expected = {'host': 'localhost', 'user': 'postgres', 'password': 'postgres', 'port': '5432'}
    assert config("postgresql") == expected


def test_data_get_problem_by_name():
    connection_params = config(section="postgresql")
    data_base = DBManager(connection_params, "codeforces_base")
    assert data_base.get_problem_by_name("problems", "test_problem", 10) == []


def test_data_get_problem_by_filter():
    connection_params = config(section="postgresql")
    data_base = DBManager(connection_params, "codeforces_base")
    assert data_base.get_problems("problems", 1000, "test", 10) == []


def test_data_prepare_data():
    connection_params = config(section="postgresql")
    data_base = DBManager(connection_params, "codeforces_base")
    assert data_base.create_database("codeforces_base") == None
    assert data_base.create_tables() == None


def test_data_insert_new_data():
    connection_params = config(section="postgresql")
    data_base = DBManager(connection_params, "codeforces_base")
    new_data = ['1872G', 'Replace With Product', None, None, 2270, 'brute force greedy math']
    assert data_base.insert_new_data("problems", new_data) == None


def test_request():
    url_problemset = "https://codeforces.com/api/problemset.problems"
    response = requests.get(url_problemset)
    assert response.status_code == 200


def test_request_empty_data():
    codeforces_data = RequestManager()
    assert codeforces_data.problems_data == []
