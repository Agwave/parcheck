# parcheck 快速入门文档

## 1 校验示例

```python
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
```

## 2 pattern 模板类型

pattern 支持的模板类型有

| 模板结构类型 |          备注          |
| :----------: | :--------------------: |
|    "dict"    | 对应 python 中的 dict  |
|    "list"    | 对应 python 中的 list  |
|    "set"     |  对应 python 中的 set  |
|    "str"     |  对应 python 中的 set  |
|    "int"     |  对应 python 中的 int  |
|   "float"    | 对应 python 中的 float |
|    "bool"    | 对应 python 中的 bool  |

### 2.1 dict 模板类型

#### 2.1.1 dict 结构

```python
{
    "struct": "dict",
    "strict": True,
    "elements": {
        "key1": "{pattern}",
        "key2": "{pattern}"
    },
    "elements_optional": {
        "key3": "{pattern}"
    }
}
```

其中 "struct" 字段为 "dict" 指明是 dict 模板类型

"strict" 字段指明是否允许未知字段的存在，为 True 表示不允许有未知的字段存在，为 False 表示允许。未指定时默认为 False

"elements" 字段指明**必要的键值信息**

"elements_optional" 字段指明**可选的键值信息**，注意该字段只能在 "strict" 为 True 时生效，因为 "strict" 为 False 时任意键名都是可选的。一般情况让 "strict" 为 True 然后使用 "elements_optional" 放宽键值是推荐的模板

#### 2.1.2 dict 示例

期望参数示例：

```python
{
    "name": "Tony",
    "age: 18,
    "gender": "male"
}
```

如果我们希望 "name", "age", "gender" **三个 key 都存在**，并且

name 对应的 value 的类型是 str，"age" 对应的 value 类型是 int，"gender" 对应的 value 类型是 str，

那么检查体的内容如下：

```python
{
    "struct": "dict",
    "strict": True,
    "elements": {
        "name": "str",
        "age": "int",
        "gender": "str"
    }
}
```

#### 2.1.3 dict 可选参数

如果 "gender" key 是可选的 key，那么检查体的内容如下：

```python
{
    "struct": "dict",
    "strict": True,
    "elements": {
        "name": "str",
        "age": "int"
    },
    "elements_optional": {
        "gender": "str"
    }
}
```

#### 2.1.4 dict 多种值类型

如果 "age" key 既可以是整型，又可以是字符串，那么检查体的内容如下：

```python
{
    "struct": "dict",
    "strict": True,
    "elements": {
        "name": "str",
        "age": ["int", "str"],
        "gender": "str"
    }
}
```

#### 2.1.5 dict 值允许 None

如果 "gender" key 既可以是字符串，又可以是 None，那么检查体的内容如下：

```python
{
    "struct": "dict",
    "strict": True,
    "elements": {
        "name": "str",
        "age": "str",
        "gender": ["str", "None"]
    }
}
```

### 2.2 list 模板类型

#### 2.2.1 list 结构

```python
{
    "struct": "list",
    "strict": True,
    "elements": "{pattern}"
}
```

#### 2.2.2 list 示例

期望参数示例：

```python
["Tony", "Tom", "Bob", "Lisa"]
```

我们希望列表里的元素类型是 str，那么检查体的内容如下：

```python
{
    "struct": "list",
	"strict": True
    "elements": "str"
}
```

#### 2.2.3 list 允许多种值类型

如果允许 list 中有 str 和 int，那么检查体的内容如下：

```python
{
    "struct": "list",
    "strict": True
    "elements": ["str", "int"]
}
```

#### 2.2.4 list 值允许 None

如果允许 list 中有 None，那么检查体的内容如下

```python
{
    "struct": "list",
    "strict": True
    "elements": ["str", "None"]
}
```

### 2.3 set 模板类型

#### 2.3.1 set 基本结构

```python
{
    "struct": "set",
    "strict": True,
    "elements": "{pattern}"
}
```

#### 2.3.2 set 示例

期望参数示例：

```python
{"Tony", "Tom", "Bob", "Lisa"}
```

我们希望列表里的元素类型是 str，那么检查体的内容如下

```python
{
    "struct": "set",
  	"strict": True,
    "elements": "str"
}
```

#### 2.3.3 set 允许多种值类型

如果允许 set 中有 str 和 int，那么检查体的内容如下：

```python
{
    "struct": "set",
    "strict": True,
    "elements": ["str", "int"]
}
```

#### 2.3.4 set 值允许 None

如果允许 set 中有 None，那么检查体的内容如下

```python
{
    "struct": "set",
    "strict": True,
    "elements": ["str", "None"]
}
```

### 2.4 str int float bool 模板类型

这几个结构比较简单，这边直接列出

```python
{
    "struct": "str"
}
```

```python
{
    "struct": "int"
}
```

```python
{
    "struct": "float"
}
```

```python
{
    "struct": "bool"
}
```

需要注意的是，之所以把 str int float bool 也都拉出来可以做成结构类型，是为了更细粒度的检查，比如说，检查字符串是否是空串

事实上，以下两种写法是等价的

```python
{
    "struct": "set",
    "elements": "str"
}
```

```python
{
    "struct": "set",
    "elements": {
        "pattern": "str"
    }
}
```

## 3 pattern 结构类型的嵌套

如果 dict 结构中的元素是 list 怎么办。假设我们的数据是这样的：

```python
{
    "name": "Tony",
    "work": {
        "company": "Google",
        "occupation": "software engineer"
    }
}
```

上面示例中 "work" 这个键的值是一个 dict，这样的数据对应的 pattern 是

```python
{
    "struct": "dict",
    "elements": {
        "name": "str",
        "work": {
            "struct": "dict",
            "elements": {
                "company": "str",
                "occupation": "str"
            }
        }
    }
}
```

可以看到，在 elements 中 "work" 键对应的值也是一个 dict 类型的结构