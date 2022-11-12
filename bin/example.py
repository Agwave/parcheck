import parcheck

data = {
    "name": "Tony",
    "age": 22
}

# 检查内容：是个 dict，且有 "name", "age" 两个键，"name" 键对应的值是 str，"age" 键对应的值是 int
pattern = {
    "struct": dict,
    "key2struct": {
        "name": str,
        "age": int
    }
}

parcheck.check(data, pattern)
