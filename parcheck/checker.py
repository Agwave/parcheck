from parcheck.patterner import pattern_struct


def check(param, pattern):
    """
    检查输入参数 param 是否满足 约束 constraint
    :param param: 参数
    :param pattern: 模板
    :return: bool
    """
    struct = pattern_struct(pattern)
    return _check_dict(param, struct)


def _check_dict(param, pattern):
    for k in pattern["key2type"]:
        if k not in param:
            return False
    for k, v in param.items():
        if k not in pattern["key2type"]:
            return False
        if not isinstance(v, pattern["key2type"][k]):
            return False
    return True


class Report(object):

    def __init__(self, result, problem=None):
        self.result = result
        self.problem = problem
