import numpy as np  ##重命名

dt = np.dtype(np.int32)  ##类型为int32，等价于i4
print(dt)
print(type(dt))
student = np.dtype([("name", "S20"), ("age", "i4"), ("marks", "f4")])  ##结构化类型对象，以元组的形式存放，名称，数据类型
print(student)
print(type(student))
# 创建一个一维数组
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
# 元素类型要相同，优先级str>float>int
arr1 = np.array([1, 2, 3, 4, 1.2])  # 打印出来的是float
print(arr1)
# 多维数组
arr2 = np.array([[1, 2, 3], [4, 5, 6], [8, 2.0, 6.5]])  # 多维数组时，可以看做是数组的嵌套
print(arr2)
# ndmin=3 最小维度是3
arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], ndmin=3)  # 生成有一个元素的三维数组，不智能
print(arr3)
# 定义参数的数据类型
arr4 = np.array([1, 2, 3], dtype='f')
print(arr4)
# 定义结构化
arr5 = np.array([("zhangsan", 15, 85.5)], dtype=student)
print(arr5)
# asarray()可以传入不同的数据类型，元组、数组均可
arr6 = np.asarray([1, 2, 3, 4, 5])
print(arr6)
# empty()函数:创建一个指定形状、数据类型但未初始化的数组
arr7 = np.empty([3, 2], dtype=int)  # 打印三行两列的二维数组数据类型为int的数组
print(arr7)
# zeros():创建指定大小的数组，数组元素以0来填充
arr8 = np.zeros([3, 2], dtype=int)  # 创建三行两列的二维数组且数据类型为int的全零数组
print(arr8)
arr9 = np.zeros(4, dtype="f")  # 创建一维数组，且有4个元素
print(arr9)
# 定义结构化的数组类型
arr10 = np.zeros([3, 2], dtype=[('x', 'i4'), ('y', 'f')])  # 前面元素为int，后面元素为float
print(arr10)
# ones():创建指定大小的数组，数据元素以1来填充
arr11 = np.ones([3, 3], dtype='f')  # 定义三行三列的二维数据
print(arr11)
# full():创建指定形状的数组，数组元素以fill_value来填充
arr12 = np.full(5, fill_value=25)  # 创建有5个元素的一维数组，并且指定数组元素为25
print(arr12)
# eye():创建对角线为1其他位置为0的数组
arr13 = np.eye(10, dtype=int)  # 创建10行10列的方阵，主对角线元素为1
print(arr13)
# numpy.arange():创建数值乏味并返回ndarray对象，根据start与stop指定的范围以及step设定的步长生成数组，一维数组
arr14 = np.arange(0, 12, 2)  # 生成一维数组，数据范围为0-12（不含12）且间隔为2
print(arr14)
# frombuffer():用于实现动态数组，接受buffer输入参数，以流的形式读入转化为ndarray对象
# buffer是字符串时，python3默认str是Unicode类型，所以要转成bytestring在原str添加b
s = b"hello,python,ni hao ya"  # 无b时，系统会报错：not 'str'
arr15 = np.frombuffer(s, dtype='S1')  # 系统默认，从头到尾
print(arr15)
arr16 = np.frombuffer(s, dtype='S1', count=5, offset=2)  # 输出5个元素，从下标为2开始输出（起始位置）
print("arr16:")
print(arr16)
# fromiter():从可迭代对象中建立ndarray对象，返回一维数组
x = [1, 2, 3, 4]
y = iter(x)
print(y)
print(type(y))
arr17 = np.fromiter(y, dtype='f')
print(arr17)
# linspace():创建一个一维函数，数组是一个等差数列构成的
arr18 = np.linspace(1, 20, 10, dtype=int)  # 创建一个初始值为1，终值为20，数组元素为10的一维数组
print(arr18)
# logspace():创建等比数列,底数默认为10
arr19 = np.logspace(1, 2, 10, dtype=int)
print(arr19)
print('splice')
# random.rand():生成[0,1）之间的随机数
arr20 = np.random.rand()  # 生成一个随机数
print(arr20)
arr21 = np.random.rand(3)  # 生成一维数组，有3个元素
print(arr21)
arr22 = np.random.rand(3, 3)  # 生成三行三列的二维数组，有9个元素
print(arr22)
arr22 = np.random.rand(3, 3, 2)  # 生成三维数组，有18个元素
print(arr22)
# random.random():生成[0,1）之间的随机数，只能生成一维
# rand.randint():生成随机数
arr23 = np.random.randint(2, 10, 5)  # 生成5个范围在2-10（不含10）的随机数
print(arr23)
# random.randn():返回一个或一组样本，具有标准正态分布
arr24 = np.random.randn(5)
print(arr24)
# random.normal():生成高斯分布的改良版密度随机数
print("高斯分布")
arr25 = np.random.normal(loc=1, scale=2, size=5)
print(arr25)

array = np.array([[3, 4], [5, 6], [7, 8]])
print(array)
print("秩为：")
print(array.ndim)
print("数组的行数和列数：")
print(array.shape)
# 修改shape值，即修改数组
array.shape = (2, 3)
print(array)
print("切片索引")
arra = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
s = slice(2, 7, 2)  # 切片的起始位置下标是2，终止位置下标是7，间隔是2
print(arra[s])

a = np.arange(15)
a.shape = (5, 3)
print(a)
print('\n')
print(a[..., 1])  # 取所有的行且列数为1的元素

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 取 0,0 1,1 2,2
print(b[[0, 1, 2], [0, 1, 2]])  # 第一个[]内为逗号前，第二个[]为逗号后，三个写一块儿，一一对应

c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# 取 0,0 1,1 2,2
print(c)
# 所取元素：0,0 0,2 3,0 3,2 竖着看
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
print('\n')
print(c[rows, cols])
print(c[1:3, 1:3])

print(c[c > 5])

d = np.array([np.nan, 1, 2, np.nan, 3, 4])
print(d)
print(d[~np.isnan(d)])  # 打印出不是np.nan
# 相同维度的数组相加
e = np.array([1, 2, 3, 4])
f = np.array([5, 6, 7, 8])
g = e + f
print(g)

h = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]])
i= np.array([1, 2, 3])
print(h+i)

#nditer:有效的多维迭代对象，可以用在数组上进行迭代
k=np.arange(12)
k.shape=(3,4)
print(k)
print('\n')
for x in np.nditer(k):
    print(x)

#广播迭代
j=np.arange(1,5)
for x,y in np.nditer([k,j]):
    print("%d:%d"%(x,y),end=',')
