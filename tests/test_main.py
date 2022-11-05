import pytest

import checker


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
    rseult = checker.check(param, constraint)
    assert rseult


if __name__ == '__main__':
    pytest.main(["-x", "-s"])
