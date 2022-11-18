from parcheck.static import Generator
from parcheck.exceptions import ParameterFormatError


def pattern(param):
    if isinstance(param, str):
        return "str"
    elif isinstance(param, bool):
        return "bool"
    elif isinstance(param, int):
        return "int"
    elif isinstance(param, float):
        return "float"
    elif param is None:
        return "None"
    elif isinstance(param, dict):
        return _dict_pattern(param)
    elif isinstance(param, list):
        return _list_pattern(param)
    elif isinstance(param, set):
        return _set_pattern(param)
    else:
        raise ParameterFormatError(Generator.PARAM_TYPE_NOT_SUPPORT)


def _dict_pattern(param):
    result = dict()
    result["struct"] = "dict"
    result["strict"] = True
    result["elements"] = dict()
    for key, value in param.items():
        result["elements"][key] = pattern(value)
    return result


def _list_pattern(param):
    result = dict()
    result["struct"] = "list"
    result["strict"] = True
    result["elements"] = list()
    for p in param:
        pt = pattern(p)
        diff = True
        for ele in result["elements"]:
            if ele == pt:
                diff = False
                break
        if diff:
            result["elements"].append(pt)
    if len(result["elements"]) == 1:
        result["elements"] = result["elements"][0]
    return result


def _set_pattern(param):
    result = dict()
    result["struct"] = "set"
    result["elements"] = list()
    result["strict"] = True
    for p in param:
        diff = True
        pt = pattern(p)
        for ele in result["elements"]:
            if ele == pt:
                diff = False
                break
        if diff:
            result["elements"].append(pt)
    if len(result["elements"]) == 1:
        result["elements"] = result["elements"][0]
    return result
