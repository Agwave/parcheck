import pytest

from pprint import pprint

import parcheck
from parcheck.checker import pattern_struct


def test_pattern():
    print()
    pattern = {
        "struct": "dict",
        "elements": {
            "language": "str",
            "book": "str",
            "price": "int"
        }
    }
    pattern = pattern_struct(pattern)
    pprint(pattern.pattern)
    pprint(pattern._elements)


def test_check_dict_1():
    param = {"language": "python", "book": "python_cookbook", "price": 10}
    pattern = {
        "struct": "dict",
        "elements": {
            "language": "str",
            "book": "str",
            "price": "int"
        }
    }
    assert parcheck.check(param, pattern)["result"]


def test_check_dict_2():
    param = {"language": "python", "book": "python_cookbook", "price": 10}
    pattern = {
        "struct": "dict",
        "elements": {
            "language": "str",
            "book": "str",
            "price": "int"
        }
    }
    assert parcheck.check(param, pattern)["result"]


def test_check_dict_3():
    param = {"language": "python", "book": "python_cookbook", "price": 10, "isgood": True}
    pattern = {
        "struct": "dict",
        "strict": True,
        "elements": {
            "language": "str",
            "book": "str",
            "price": "int"
        },
        "elements_optional": {
            "isgood": "bool"
        }
    }
    assert parcheck.check(param, pattern)["result"]


def test_check_dict_4():
    param = {"language": "python", "book": "python_cookbook", "price": 10}
    pattern = {
        "struct": "dict",
        "strict": True,
        "elements": {
            "language": "str",
            "book": "str",
            "price": ["str", "bool", "int"]
        }
    }
    assert parcheck.check(param, pattern)["result"]


def test_check_dict_5():
    param = {"language": "python", "book": "python_cookbook", "price": None}
    pattern = {
        "struct": "dict",
        "strict": True,
        "elements": {
            "language": "str",
            "book": "str",
            "price": ["int", "None"]
        }
    }
    assert parcheck.check(param, pattern)["result"]


if __name__ == '__main__':
    pytest.main(["-x", "-s"])
