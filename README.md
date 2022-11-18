# python 参数检查器：parcheck

**这是一个让你大幅提高检查效率的好工具**

## 1 一句话介绍

**parcheck** 是一个**轻量级**的、**简单**的、**易于使用**的参数检查工具

## 2 parcheck 带来的好处

假设我们有一个函数或者接口，它的输入样例比较复杂，比如像下面这样

```python
{
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
          "项目时长（月）": 12
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
          "项目时长（月）": 6
        }
      ]
    }
  ]
}
```

假设我们需要

**检查每一个键是否存在**，比如 "名字"、"年龄"、"职业经历" 等是否存在（包括 "职业经历" 的信息检查）

**检查每一个键对应的值的数据类型是否正确**，比如 "名字" 对应的值是不是 "字符串"，"职业经历" 对应的值是不是我们期望的格式等

如果纯手写检查，无疑是很**浪费时间**且**无聊**的，但是如果使用 **parcheck**，我们就只需要几行代码便可实现检查

```python
import parcheck

sample = "{参数样例}"
data = "{待检查的参数}"

pattern = parcheck.pattern(sample)  # 生成校验模板
result = parcheck.check(data, pattern)  # 根据校验模板对新来的参数进行检查，返回检查结果
```

## 3 使用场景举例：web 接口数据参数检查

很多时候，web 接口通过 json 的方式进行传参。

将 json 转成 python 数据类型后，我们常常需要检查数据的基本格式是否正确，以方便后续处理。

尤其是对于提供给外部使用的接口，往往都需要非常**严格检查**。

但是有时候，传递的数据可能层层嵌套，非常复杂，如果是手动一个个写代码去检查，是非常耗时的。

这个时候就可以用到 **parcheck**，**parcheck** 可以帮助我们进行非常便捷的检查。

## 4 一个简单的检查示例

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

打印结果：

```json
{'result': False, 'messge': "'22' 不是 'str' 类型"}
```

可以看到，parcheck 检查出来参数中 "age" 对应的键不是字符串类型

## 5 parcheck 的优势

① 完善的检查失败的错误提示，方便找到参数错误之处

② 参数检查非常方便，一行代码进行参数检查

## 6 核心 API

parcheck 非常容易使用，它只有**两个**核心的 API。

一个用来进行**参数检查**

一个用来**自动化生成参数检查模板**

### 6.1 parcheck.check

使用 **parcheck.check** 进行参数检查，它有两个参数 param 和 pattern

其中，**param** 是待检查的参数，**pattern** 是我们事先准备好的检查模板

### 6.2 parcheck.pattern

使用 **parcheck.pattern** 自动生成检查模板，它有一个参数 param

其中，**param** 是一个参数样例

这个接口会根据这个参数样例**自动生成**对应的检查模板

## 7 推荐使用方法

① 先使用样例数据生成检查模板 pattern

② 如果有更细节的需求，可以调整生成的 pattern，存到模板配置中

③ 使用 parcheck 和模板配置进行检查

## 8 下载方法

```shell
pip install parcheck
```

## 9 其他


项目地址：https://github.com/Agwave/parcheck.git

目前项目完成初版，项目文档见项目 **docs** 目录，更多使用例子见 **bin** 目录中的 **example** 相关文件

欢迎使用

版本初次发布，肯定有不足和需要完善的点，欢迎提问题

之前没有找到类似的方便的工具，所以开个头，欢迎一起参与贡献代码和完善功能



# 附：简单文档

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
"str"
```

```python
{
    "struct": "str"
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
