import json
import pytest
import parse


class TestData:
    """
        Класс TestData загружает входные и выходные данные
        для передачи через фикстуру в тестовую функцию
    """
    def __init__(self):
        with open('in.json', encoding='utf-8') as f:
            self.in_data = json.load(f)
        with open('out.json', encoding='utf-8') as f:
            self.out_data = json.load(f)


@pytest.fixture(scope='function')
def test_data():
    return TestData()


def test_parse(test_data):
    assert parse.parse(test_data.in_data) == test_data.out_data, 'Parsing and convertation has complited unsuccessfully!'


if __name__ == '__main__':
    pass
