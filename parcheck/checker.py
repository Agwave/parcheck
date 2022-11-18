import abc

import parcheck.exceptions as ex
from parcheck.static import PatterKey, Message, Report
from parcheck.tools import dict_merged


def check(param, pattern):
    """
    检查输入参数 param 是否满足 约束 constraint
    :param param: 参数
    :param pattern: 模板
    :return: bool
    """
    struct = pattern_struct(pattern)
    return struct.check(param)


def pattern_struct(pattern):
    if isinstance(pattern, str):
        return _pattern_object_by_str(pattern)
    elif isinstance(pattern, dict):
        return _pattern_object_by_dict(pattern)
    elif isinstance(pattern, list):
        return _pattern_object_by_list(pattern)
    else:
        raise ex.PatternFormatError(Message.PATTERN_NOT_DICT_STR_LIST)


def _pattern_object_by_str(pattern):
    if pattern == "dist":
        return DictStruct({"struct": pattern})
    elif pattern == "list":
        return ListStruct({"struct": pattern})
    elif pattern == "set":
        return SetStruct({"struct": pattern})
    elif pattern == "str":
        return StrStruct({"struct": pattern})
    elif pattern == "int":
        return IntStruct({"struct": pattern})
    elif pattern == "float":
        return FloatStruct({"struct": pattern})
    elif pattern == "bool":
        return BoolStruct({"struct": pattern})
    elif pattern == "None":
        return NoneStruct({"struct": pattern})
    else:
        raise ex.PatternFormatError(Message.PATTERN_STRUCT_NOT_FOUND)


def _pattern_object_by_dict(pattern):
    if PatterKey.STRUCT_KEY not in pattern:
        raise ex.PatternFormatError(Message.STRUCT_KEY_NOT_FOUND)
    name = pattern[PatterKey.STRUCT_KEY]
    if name == "dict":
        return DictStruct(pattern)
    elif name == "list":
        return ListStruct(pattern)
    elif name == "set":
        return SetStruct(pattern)
    elif name == "str":
        return StrStruct(pattern)
    elif name == "int":
        return IntStruct(pattern)
    elif name == "float":
        return FloatStruct(pattern)
    elif name == "bool":
        return BoolStruct(pattern)
    elif name == "None":
        return NoneStruct(pattern)
    else:
        raise ex.PatternFormatError(Message.PATTERN_VALUE_NOT_FOUND.format(name))


def _pattern_object_by_list(pattern):
    for p in pattern:
        if not isinstance(p, (str, dict)):
            raise ex.PatternFormatError(Message.LIST_PATTERN_ELEMENTS_STR_LIST)
    return [pattern_struct(p) for p in pattern]


class PatternStruct(object):

    def __init__(self, pattern):
        self.pattern = pattern
        self.struct = pattern[PatterKey.STRUCT_KEY]

    @abc.abstractmethod
    def check(self, param):
        pass

    @staticmethod
    def _check_value(value_element, value):
        if not isinstance(value_element, list):
            if not value_element.check(value)["result"]:
                return value_element.check(value)
        else:
            match = False
            for v in value_element:
                if v.check(value)["result"]:
                    match = True
                    break
            if not match:
                return _make_report(False, Report.DICT_PARAM_VALUE_NOT_A_EXCEPT_TYPE.format(value))
        return _make_report(True)


def _make_report(result, message=None):
    return {
        "result": result,
        "message": message
    }


class DictStruct(PatternStruct):

    def __init__(self, pattern):
        super().__init__(pattern)
        self._strict = None
        self._elements = None
        self._options = None
        self._make()

    def _make(self):
        self._strict = self.pattern.get(PatterKey.STRICT_KEY, False)
        self._elements = self._make_elements(PatterKey.ELEMENTS_KEY)
        if self._strict:
            self._options = self._make_elements(PatterKey.ELEMENTS_OPTIONAL_KEY)

    def _make_elements(self, pattern_key):
        result = dict()
        elements = self.pattern.get(pattern_key, dict())
        if not isinstance(elements, dict):
            raise ex.PatternFormatError(Message.FIELD_VALUE_TYPE_ERROR.format(pattern_key))
        for key, value in elements.items():
            result[key] = pattern_struct(value)
        return result

    def check(self, param):
        if not isinstance(param, dict):
            return _make_report(False, Report.PARAM_NOT_A_EXCEPT_TYPE.format(param, "dict"))
        if not self._check_elements_key_value(param)["result"]:
            return self._check_elements_key_value(param)
        if self._strict and (not self._check_elements_options_key_value(param)["result"]):
            return self._check_elements_options_key_value(param)
        return _make_report(True)

    def _check_elements_key_value(self, param):
        for key, value_element in self._elements.items():
            if key not in param:
                return _make_report(False, Report.DICT_MISSING_KEY.format(param, key))
            if not self._check_value(value_element, param[key])["result"]:
                return self._check_value(value_element, param[key])
        return _make_report(True)

    def _check_elements_options_key_value(self, param):
        compelete_elements = dict_merged(self._options, self._elements)
        for key, value in param.items():
            if key not in compelete_elements:
                return _make_report(False, Report.DICT_PARAM_KEY_UNKNOWN.format(param, key))
            value_element = compelete_elements[key]
            if not self._check_value(value_element, value)["result"]:
                return self._check_value(value_element, value)
        return _make_report(True)


class ListStruct(PatternStruct):

    def __init__(self, pattern):
        super().__init__(pattern)
        self._strict = None
        self._elements = None
        self._make()

    def _make(self):
        self._strict = self.pattern.get("strict", True)
        if self._strict:
            elements = self.pattern.get("elements", None)
            if elements is not None:
                self._elements = pattern_struct(elements)

    def check(self, param):
        if not isinstance(param, list):
            return _make_report(False, Report.PARAM_NOT_A_EXCEPT_TYPE.format(param, "list"))
        if self._strict and self._elements is not None:
            for p in param:
                if not self._check_value(self._elements, p)["result"]:
                    return self._check_value(self._elements, p)
        return _make_report(True)


class SetStruct(PatternStruct):

    def __init__(self, pattern):
        super().__init__(pattern)
        self._strict = None
        self._elements = None
        self._make()

    def _make(self):
        self._strict = self.pattern.get("strict", True)
        if self._strict:
            elements = self.pattern.get("elements", None)
            if elements is not None:
                self._elements = pattern_struct(elements)

    def check(self, param):
        if not isinstance(param, set):
            return _make_report(False, Report.PARAM_NOT_A_EXCEPT_TYPE.format(param, "set"))
        if self._strict and self._elements is not None:
            for p in param:
                if not self._check_value(self._elements, p)["result"]:
                    return self._check_value(self._elements, p)
        return _make_report(True)


class StrStruct(PatternStruct):

    def __init__(self, pattern):
        super().__init__(pattern)

    def check(self, param):
        if not isinstance(param, str):
            return _make_report(False, Report.PARAM_NOT_A_EXCEPT_TYPE.format(param, "str"))
        return _make_report(True)


class IntStruct(PatternStruct):

    def __init__(self, pattern):
        super().__init__(pattern)

    def check(self, param):
        if not isinstance(param, int):
            return _make_report(False, Report.PARAM_NOT_A_EXCEPT_TYPE.format(param, "int"))
        return _make_report(True)


class FloatStruct(PatternStruct):

    def __init__(self, pattern):
        super().__init__(pattern)

    def check(self, param):
        if not isinstance(param, float):
            return _make_report(False, Report.PARAM_NOT_A_EXCEPT_TYPE.format(param, "float"))
        return _make_report(True)


class BoolStruct(PatternStruct):

    def __init__(self, pattern):
        super().__init__(pattern)

    def check(self, param):
        if not isinstance(param, bool):
            return _make_report(False, Report.PARAM_NOT_A_EXCEPT_TYPE.format(param, "bool"))
        return _make_report(True)


class NoneStruct(PatternStruct):

    def __init__(self, pattern):
        super().__init__(pattern)

    def check(self, param):
        if param is not None:
            return _make_report(False, Report.PARAM_NOT_A_EXCEPT_TYPE.format(param, "None"))
        return _make_report(True)
