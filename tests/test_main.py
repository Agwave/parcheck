import pytest

from pprint import pprint

import parcheck
from parcheck.patterner import pattern_struct


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


def test_check():
    param = {"language": "python", "book": "python_cookbook", "price": 10}
    constraint = {
        "type": dict,
        "key2type": {
            "language": str,
            "book": str,
            "price": int
        }
    }
    rseult = parcheck.check(param, constraint)
    assert rseult


if __name__ == '__main__':
    pytest.main(["-x", "-s"])
