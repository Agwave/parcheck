import pytest

from pprint import pprint

import parcheck
from parcheck.checker import pattern_struct, StrStruct, IntStruct, BoolStruct, NoneStruct, FloatStruct, ListStruct, \
    SetStruct, DictStruct
from parcheck.patterner import pattern as pt


def test_pattern_dict_1():
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
    pprint(pattern)
    pprint(pattern._elements)
    assert isinstance(pattern, DictStruct)
    assert isinstance(pattern._elements["book"], StrStruct)
    assert isinstance(pattern._elements["language"], StrStruct)
    assert isinstance(pattern._elements["price"], IntStruct)


def test_pattern_dict_2():
    print()
    pattern = {
        "struct": "dict",
        "strict": True,
        "elements": {
            "language": "str",
            "book": "str",
            "price": "int"
        },
        "elements_optional": {
            "gender": "float"
        }
    }
    pattern = pattern_struct(pattern)
    pprint(pattern._elements)
    assert isinstance(pattern._options["gender"], FloatStruct)


def test_pattern_dict_3():
    print()
    pattern = {
        "struct": "dict",
        "elements": {
            "language": "str",
            "book": "str",
            "price": ["int", "str"]
        }
    }
    pattern = pattern_struct(pattern)
    pprint(pattern._elements)
    assert isinstance(pattern._elements["price"], list)
    assert isinstance(pattern._elements["price"][0], IntStruct)
    assert isinstance(pattern._elements["price"][1], StrStruct)


def test_pattern_dict_4():
    print()
    pattern = {
        "struct": "dict",
        "elements": {
            "language": "str",
            "book": "str",
            "price": "None"
        }
    }
    pattern = pattern_struct(pattern)
    pprint(pattern._elements)
    assert isinstance(pattern._elements["price"], NoneStruct)


def test_pattern_dict_5():
    print()
    pattern = {
        "struct": "dict"
    }
    pattern = pattern_struct(pattern)
    pprint(pattern._elements)
    assert not pattern._elements


def test_pattern_list_1():
    print()
    pattern = {
        "struct": "list",
        "strict": True,
        "elements": "str"
    }
    pattern = pattern_struct(pattern)
    pprint(pattern._elements)
    assert isinstance(pattern._elements, StrStruct)


def test_pattern_list_2():
    print()
    pattern = {
        "struct": "list",
        "strict": True,
        "elements": ["str", "int", "None"]
    }
    pattern = pattern_struct(pattern)
    pprint(pattern._elements)
    assert isinstance(pattern._elements, list)
    assert isinstance(pattern._elements[0], StrStruct)
    assert isinstance(pattern._elements[1], IntStruct)
    assert isinstance(pattern._elements[2], NoneStruct)


def test_pattern_list_3():
    print()
    pattern = {
        "struct": "list"
    }
    pattern = pattern_struct(pattern)
    pprint(pattern._elements)
    assert pattern._elements is None


def test_pattern_list_4():
    print()
    pattern = "list"
    pattern = pattern_struct(pattern)
    pprint(pattern)
    pprint(pattern._elements)
    assert isinstance(pattern, ListStruct)
    assert pattern._elements is None


def test_pattern_set_1():
    print()
    pattern = {
        "struct": "set",
        "strict": True,
        "elements": "str"
    }
    pattern = pattern_struct(pattern)
    pprint(pattern._elements)
    assert isinstance(pattern._elements, StrStruct)


def test_pattern_set_2():
    print()
    pattern = {
        "struct": "set",
        "strict": True,
        "elements": ["str", "int", "None"]
    }
    pattern = pattern_struct(pattern)
    pprint(pattern._elements)
    assert isinstance(pattern._elements[2], NoneStruct)
    assert isinstance(pattern._elements[1], IntStruct)
    assert isinstance(pattern._elements[0], StrStruct)
    assert isinstance(pattern._elements, list)


def test_pattern_set_3():
    print()
    pattern = {
        "struct": "set"
    }
    pattern = pattern_struct(pattern)
    pprint(pattern._elements)
    assert pattern._elements is None


def test_pattern_set_4():
    print()
    pattern = "set"
    pattern = pattern_struct(pattern)
    pprint(pattern)
    pprint(pattern._elements)
    assert isinstance(pattern, SetStruct)
    assert pattern._elements is None


def test_pattern_str():
    print()
    pattern = "str"
    pattern = pattern_struct(pattern)
    print(pattern)
    assert isinstance(pattern, StrStruct)


def test_pattern_int():
    print()
    pattern = "int"
    pattern = pattern_struct(pattern)
    print(pattern)
    assert isinstance(pattern, IntStruct)


def test_pattern_float():
    print()
    pattern = "float"
    pattern = pattern_struct(pattern)
    print(pattern)
    assert isinstance(pattern, FloatStruct)


def test_pattern_bool():
    print()
    pattern = "bool"
    pattern = pattern_struct(pattern)
    print(pattern)
    assert isinstance(pattern, BoolStruct)


def test_pattern_none():
    print()
    pattern = "None"
    pattern = pattern_struct(pattern)
    print(pattern)
    assert isinstance(pattern, NoneStruct)


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


def test_check_dict_6():
    print()
    param = {"language": "python"}
    pattern = {
        "struct": "dict",
        "strict": True,
        "elements": {
            "language": "str",
            "book": "str"
        }
    }
    print(parcheck.check(param, pattern))
    assert parcheck.check(param, pattern) == {'result': False, 'message': "'{'language': 'python'}' 中没有 'book'"}


def test_check_dict_7():
    print()
    param = {"language": "python", "book": "Effective Python"}
    pattern = {
        "struct": "dict",
        "strict": True,
        "elements": {
            "language": "str"
        }
    }
    print(parcheck.check(param, pattern))
    assert parcheck.check(param, pattern) == {
        'result': False, 'message': "'{'language': 'python', 'book': 'Effective Python'}' 中有未知的 key 'book'"}


def test_check_list_1():
    param = ["python", "cpp", 1]
    pattern = {
        "struct": "list"
    }
    assert parcheck.check(param, pattern)["result"]


def test_check_list_2():
    param = ["python", "cpp", 1]
    pattern = {
        "struct": "list",
        "strict": True,
        "elements": ["str", "int"]
    }
    assert parcheck.check(param, pattern)["result"]


def test_check_list_3():
    param = ["python", "cpp", 1, None]
    pattern = {
        "struct": "list",
        "strict": True,
        "elements": ["str", "None", "int"]
    }
    assert parcheck.check(param, pattern)["result"]


def test_check_list_4():
    param = ["python", "cpp"]
    pattern = {
        "struct": "list",
        "strict": True,
        "elements": "str"
    }
    assert parcheck.check(param, pattern)["result"]


def test_check_list_5():
    print()
    param = ["python", "cpp", 1]
    pattern = {
        "struct": "list",
        "strict": True,
        "elements": ["str", "bool"]
    }
    print(parcheck.check(param, pattern))
    assert parcheck.check(param, pattern) == {'result': False, 'message': "'1' 不符合期望的模板"}


def test_check_set_1():
    param = {"python", "cpp"}
    pattern = {
        "struct": "set"
    }
    assert parcheck.check(param, pattern)["result"]


def test_check_set_2():
    param = {"python", "cpp"}
    pattern = {
        "struct": "set",
        "strict": True,
        "elements": "str"
    }
    assert parcheck.check(param, pattern)["result"]


def test_check_set_3():
    param = {"python", "cpp", 1}
    pattern = {
        "struct": "set",
        "strict": True,
        "elements": ["str", "int"]
    }
    assert parcheck.check(param, pattern)["result"]


def test_check_set_4():
    param = {"python", "cpp", None}
    pattern = {
        "struct": "set",
        "strict": True,
        "elements": ["str", "None"]
    }
    assert parcheck.check(param, pattern)["result"]


def test_check_str():
    print()
    param = "python"
    pattern = "str"
    assert parcheck.check(param, pattern)["result"]
    pattern = "int"
    pprint(parcheck.check(param, pattern))
    assert parcheck.check(param, pattern) == {'message': "'python' 不是 'int' 类型", 'result': False}


def test_check_int():
    param = 123
    pattern = "int"
    assert parcheck.check(param, pattern)["result"]


def test_check_float():
    param = 3.14
    pattern = "float"
    assert parcheck.check(param, pattern)["result"]


def test_check_bool():
    param = True
    pattern = "bool"
    assert parcheck.check(param, pattern)["result"]


def test_check_none():
    param = None
    pattern = "None"
    assert parcheck.check(param, pattern)["result"]


def test_generate_pattern_1():
    print()
    param = {"language": "python", "book": "python_cookbook", "price": 10}
    pprint(pt(param))
    assert pt(param) == {'elements': {'book': 'str', 'language': 'str', 'price': 'int'},
                         'strict': True,
                         'struct': 'dict'}


def test_generate_pattern_2():
    print()
    param = ["python", 123]
    pprint(pt(param))
    assert pt(param) == {'elements': ['str', 'int'], 'strict': True, 'struct': 'list'}


def test_generate_pattern_3():
    print()
    param = {"pattern", True, None}
    pprint(pt(param))
    assert set(pt(param)["elements"]) == {'str', 'bool', 'None'}


def test_generate_pattern_4():
    print()
    param = "python"
    pprint(pt(param))
    assert pt(param) == 'str'


def test_generate_pattern_5():
    print()
    param = None
    pprint(pt(param))
    assert pt(param) == "None"


if __name__ == '__main__':
    pytest.main(["-x", "-s", "-v"])
