import parcheck

data = {
    "name": "Tony",
    "age": 22
}

# 可以手写期望的检查模板：是个 dict，且有 "name", "age" 两个键，"name" 键对应的值是 str，"age" 键对应的值是 str
pattern = {
    "struct": "dict",
    "elements": {
        "name": "str",
        "age": "str"
    }
}

report = parcheck.check(data, pattern)  # 根据检查模板进行检查，返回检查报告
print(report)  # 打印检查结果
