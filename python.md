- **命名约定**：类名通常使用 `CapWords` 约定（也称为 CamelCase，因为名称中间的大写字母看起来像驼峰）编写。方法名称遵循使用下划线分隔的小写单词命名函数的标准约定。

- ### 数据类型

  - #### `string`

    - 索引
    - `+`
    - `*` ：生成重复的字符串
    - `str()` ：转为字符串
    - `upper()`：a->A
    - `lower()`：A->a
    - `strip()`：去掉空格及多余字符
    - `split()`：按指定字符串分割字符串
    - `repleace()`：字符串替换
    - 格式化
      - `format()`
        - 内部槽：`{<参数序号>:<格式控制标记>}`
        - <填充><对齐><宽度><.精度><类型>

  - #### 字典

    - `init`
      - `dic = {}`
      - `dic = dict()`
      - `dic = dict([("a",2),("b",4)])`
      - `dic = dict(a=2,b=4)  # use **args` 
    - find
      - []  #不存在会报错
      - `get(key,non-return)`
      - `in`
    - add
      - []
      - `update({kay1: value1, kay2 : value2})`
    - delete
      - `del dic[key]`
      - `pop(key)`
    - 遍历 
      - `keys(),values(),items()`

  - #### 元组

    - 创建
      - `tu = (1,3,4,5)`

  - #### `list()`

    - 创建
      - ls = list()
      - ls = []
    - 索引
    - method
      - append
      - `insert(i, x)` insert x in i position
      - `pop(i)` get and remove `ls[i]`
      - `remove(x)` remove first x
      - `reverse()` reverse x

  - #### `set()`

    - `add()`
    - `clear()`
    - `copy()`
    - `remove()`  not in raise error
    - `discard()` not in noting
    - 

  - #### `deque`

    - method
      - `appendleft()`
      - `append`()
      - 

  - `Counter()`

    - 专门用来计数的字典

  - `defaultdict`(lambda: default-value)

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
    - 将function应用于`iterable`中的每一个参数
  - `reduce(function, iterable[, initialzer])`
    - 利用function将`iterable`中的元素合起来

- ### 列表推导式

  - `<expression> for item in iterable <if optional_condition>`
  - `eg: {value: key for key, value in dict1.item if key>='0'}`

- ### io

  - #### csv

    - `improt csv`
    - read
      - `csv.reader()`
      - `for row in reader()`
    - write
      - `csv.DicWriter()`
      - `f.writeheader(headline)`
      - `f.writerows(rows)`

  - #### os

    - 获取环境变量`os.environ.get('key')`
    - dir
      - 遍历`os.listdir(path='.')`
      - 创建`os.mkdir()`
      - 删除`os.rmdir()`
    - path
      - 查看当前的绝对路径`os.path.abspath()`
      - 多个目录路径合并`os.path.join()`
      - 路径拆分，把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：` os.path.split(path)`
      - 文件扩展名获取： `os.path.splitext(path)`  
      - 文件确认`os.isfile(path)`

- ### OOP

  - 属性(Attribute): 类里面用于描述所有对象共同特征的变量或数据。比如学生的名字和分数。
  
  - 方法(Method): 类里面的函数，用来区别类外面的函数, 用来实现某些功能。比如打印出学生的名字和分数。
  
  - 类变量(class variables)与实例变量（instance variables）
    - 类变量是属于整个类的变量
    
    - 实例变量是动态分配的
    
      ```python
      class A():
          pass
      s = A()
      s.a = 3
      ```
    
      此时a是实例变量（实例属性）
    
  - 类方法(class method)
    - `@classmethod`
    - `cls` -> `self`
    
  - 类的私有属性和私有方法
    - 以`__`开头
      - 在`init`中定义，转义（自动替换）成`_类名__变量名`
    
  - 继承(Inheritance)
    - `class ChildClass(ParentClass)`
    - 手动调用父类的构造函数
    - 调用父类的方法时需要加上`self`参数变量，可以使用`super`简化
    
  - 静态变量和静态方法
    - 无须显式地声明静态变量
    
      ```python
      class A():
          a = 0
          def __init__(self):
              self.b = 1
      ```
    
      a为静态变量，为所有该类的实例共有
    
    - 使用`@staticmethod`声明静态函数
    
  - 修饰
    - `@property` 将函数伪装成属性
    
  - 方法
  
    - `isinstance(实例,类)`  判断实例是否是该类的实例
    - `dir(实例)` 查看所具有的属性和方法