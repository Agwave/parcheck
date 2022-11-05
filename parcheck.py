

def check(param, constraint):
    """
    检查输入参数 param 是否满足 约束 constraint
    :param param: 参数
    :param constraint: 约束
    :return: bool
    """
    return check_dict(param, constraint)


def check_dict(param, constraint):
    for k in constraint["key2type"]:
        if k not in param:
            return False
    for k, v in param.items():
        if k not in constraint["key2type"]:
            return False
        if not isinstance(v, constraint["key2type"][k]):
            return False
    return True
