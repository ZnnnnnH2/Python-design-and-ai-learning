- **命名约定**：类名通常使用 `CapWords` 约定（也称为 CamelCase，因为名称中间的大写字母看起来像驼峰）编写。方法名称遵循使用下划线分隔的小写单词命名函数的标准约定。

- ### 数据类型

  - #### 字典

    - `init`
      - `dic = {}`
      - `dic = dict()`
      - `dic = dict([("a",2),("b",4)])`
      - `dic = dict(a=2,b=4)`
    - find
      - []  #不存在会报错
      - `get(key,non-return)`
      - `in`
    - add
      - []
    - change
      - []
    - delete
      - `del dic[key]`
    - 遍历 
      - `keys(),values(),items()`
  - #### 元组

    - 创建
      - `tu = (1,3,4,5)`
  - #### 列表 

    - 创建
      - ls = list()
      - ls = []
    - 索引
    - method
      - append
      - 
  - #### 集合

    - 创建
      - s = {}

  - #### deque

    - method
      - `appendleft()`
      - `append`()
      - 

  - ### `Counter()`

    - 专门用来计数的字典

  - ### `defaultdict`(lambda: default-value)

    - 有默认值的字典
    - 

- ### 函数

  - 传参
    - `*arg`
      - 可变长度的参数，作为元组传入
    - ``**arg``
      - 打包成字典传入

- ### 高阶函数

  - `filter(function, iterable)`
    - 功能：筛选器
    - 返回一个可遍历对象，使用list(filter())配合
    - `eg: odd = list(filter(lambda x : x%2==0, data))`
  - `map(function,iterable,...)`
    - 将function应用于iterable中的每一个参数
  - `reduce(function, iterable[, initialzer])`
    - 利用function将`iterable`中的元素合起来

- ### 列表推导式

  - `<expression> for item in iterable <if optional_condition>`
  - `eg: {value: key for key, value in dict1.item if key>='0'}`