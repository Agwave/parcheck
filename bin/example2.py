import parcheck

from pprint import pprint


sample = {
    "名字": "大壮",
    "年龄": 18,
    "爱好": [
        "羽毛球",
        "足球"
    ],
    "职业经历": [
        {
            "时间": "2022",
            "公司": "google",
            "职位": "数据分析",
            "项目": [
                {
                    "项目名": "图数据分析",
                    "项目介绍": "对图数据进行分析",
                    "项目时长（日）": 120
                }
            ]
        },
        {
            "时间": "2021",
            "公司": "facebook",
            "职位": "数据开发",
            "项目": [
                {
                    "项目名": "流数据分析推荐",
                    "项目介绍": "通过实时分析数据进行相关推荐",
                    "项目时长（日）": 60
                }
            ]
        }
    ]
}
data = {
    "名字": "小红",
    "年龄": 18,
    "爱好": [
        "跳绳",
        "瑜伽"
    ],
    "职业经历": [
        {
            "时间": "2021",
            "公司": "baidu",
            "职位": "python开发",
            "项目": [
                {
                    "项目名": "图分析软件",
                    "项目介绍": "实现具有图分析功能的软件",
                    "项目时长（月）": 6
                }
            ]
        }
    ]
}
pattern = parcheck.pattern(sample)
pprint(pattern)
assert pattern == {'elements': {'名字': 'str',
                                '年龄': 'int',
                                '爱好': {'elements': 'str', 'strict': True, 'struct': 'list'},
                                '职业经历': {'elements': {'elements': {'公司': 'str',
                                                                   '时间': 'str',
                                                                   '职位': 'str',
                                                                   '项目': {'elements': {'elements': {
                                                                       '项目介绍': 'str',
                                                                       '项目名': 'str',
                                                                       '项目时长（日）': 'int'},
                                                                       'strict': True,
                                                                       'struct': 'dict'},
                                                                       'strict': True,
                                                                       'struct': 'list'}},
                                                      'strict': True,
                                                      'struct': 'dict'},
                                         'strict': True,
                                         'struct': 'list'}},
                   'strict': True,
                   'struct': 'dict'}
pprint(parcheck.check(data, pattern))
assert parcheck.check(data, pattern) == {'messge': "'{'项目名': '图分析软件', '项目介绍': '实现具有图分析功能的软件', "
                                                   "'项目时长（月）': 6}' 中没有 "
                                                   "'项目时长（日）'",
                                         'result': False}
