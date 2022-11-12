# python 参数检查器：parcheck

## 1 校验示例

```python
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
```

## 2 pattern 结构

### 2.1 dict

#### 2.1.1 dict 基本结构

```python
{
    "struct": dict,
    "key2struct": {
        "key1": "{struct}",
        "key2": "{struct}"
    },
    "key2struct_optional": {
        "key3": "{struct}"
    }
}
```

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
    "struct": dict,
    "key2struct": {
        "name": str,
        "age": int,
        "gender": str
    }
}
```

如果 "gender" key 是可选的 key，那么检查体的内容如下：

```python
{
    "struct": dict,
    "key2struct": {
        "name": str,
        "age": int
    },
    "key2struct_optional": {
        "gender": str
    }
}
```

### 2.2 list

#### 2.2.1 list 基本结构

```python
{
    "struct": list,
    "type": "{struct}"
}
```

#### 2.2.2 list 示例

期望参数示例：

```python
["Tony", "Tom", "Bob", "Lisa"]
```

我们希望列表里的元素类型是 str，那么检查体的内容如下

```python
{
    "struct": list,
    "type": str
}
```

## 3 推荐使用方法

① 先使用样例数据生成模板 pattern

② 根据自己更细节地需求，调整生成的 pattern，存到配置中

③ 根据配置 和 parcheck.check 进行校验

