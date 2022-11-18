import parcheck

data = {
    "name": "Tony",
    "age": 22
}

# 自定义检查模板：是个 dict，且有 "name", "age" 两个键，"name" 键对应的值是 str，"age" 键对应的值是 int
pattern = {
    "struct": "dict",
    "elements": {
        "name": "str",
        "age": "int"
    }
}

report = parcheck.check(data, pattern)  # 根据检查模板进行检查，返回检查报告
print(report["result"])  # 打印检查结果
