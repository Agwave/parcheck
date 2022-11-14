import parcheck.exceptions as ex
from parcheck.static import PatterKey, Message


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
        return DictStruct({"struct": pattern, "strict": False})
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
    else:
        raise ex.PatternFormatError(Message.PATTERN_STRUCT_NOT_FOUND)


def _pattern_object_by_dict(pattern):
    if PatterKey.STRUCT_KEY not in pattern:
        raise ex.PatternFormatError(Message.STRUCT_KEY_NOT_FOUND)
    if PatterKey.ELEMENTS_KEY not in pattern:
        raise ex.PatternFormatError(Message.ELEMENTS_KEY_NOT_FOUND)
    name = pattern[PatterKey.STRUCT_KEY]
    if name == "dict":
        return DictStruct(pattern)
    elif name == "list":
        return ListStruct(pattern)
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
        self._struct = pattern[PatterKey.STRUCT_KEY]


class DictStruct(PatternStruct):

    def __init__(self, pattern):
        super().__init__(pattern)
        self._elements = None
        self.elements_options = None
        self._make()

    def _make(self):
        elements = self.pattern[PatterKey.ELEMENTS_KEY]
        if not isinstance(elements, dict):
            raise ex.PatternFormatError(Message.ELEMENTS_VALUE_TYPE_ERROR)
        self._elements = dict()
        for key, value in elements.items():
            self._elements[key] = pattern_struct(value)


class ListStruct(PatternStruct):

    def __init__(self, pattern):
        super().__init__(pattern)
        self._elements = None
        self._make()

    def _make(self):
        self._elements = self.pattern[PatterKey.ELEMENTS_KEY]


class SetStruct(PatternStruct):

    def __init__(self, pattern):
        super().__init__(pattern)
        self._elements = None

    def _make(self):
        self._elements = self.pattern[PatterKey.ELEMENTS_KEY]


class StrStruct(PatternStruct):
    
    def __init__(self, pattern):
        super().__init__(pattern)


class IntStruct(PatternStruct):

    def __init__(self, pattern):
        super().__init__(pattern)


class FloatStruct(PatternStruct):

    def __init__(self, pattern):
        super().__init__(pattern)


class BoolStruct(PatternStruct):

    def __init__(self, pattern):
        super().__init__(pattern)
