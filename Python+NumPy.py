
# coding: utf-8

# # Python科学计算：用NumPy快速处理数据

# NumPy是Python中使用最多的第三方库，也是SciPy, Pandas等数据科学的基础库。NumPy提供的数据结构是Python数据分析的基础。NumPy 通常与 SciPy（Scientific Python）和 Matplotlib（绘图库）一起使用， 这种组合广泛用于替代 MatLab，是一个强大的科学计算环境，有助于我们通过 Python 学习数据科学或者机器学习。
# 
# ## 让科学计算更高效
# 
# - NumPy数组结构 vs. Python的列表 list
# 
#   NumPy数组存储在一个均匀连续的内存块中，数组计算遍历所有元素，无需查找内存地址，节省计算资源。
# 
#   List 保存的是对象的指针，list 的元素在内存中存储分散，计算时需要查找内存地址，浪费内存和计算时间。
# 
# - 内存访问模式中，缓存会直接把字节块从RAM 加载到CPU寄存器中
# 
# - 矩阵计算可以采用多线程方式，充分利用多核CPU计算资源，大大提高效率
# 
# - 技巧：避免隐式拷贝，而是采用就地操作的方式，如 `x*=2`，而不是 `y=x*2`，速度能快到2倍甚至更多。
# 
# 
# ## ndarray (N-dimensional array object) 多维数组
# 
# 维数：秩 rank，描述的是轴的数量，轴为每个线性的数组
# 
# ### 1 创建数组：

# In[27]:


# -*- coding: utf-8 -*-

# 引入NumPy库
import numpy as np

# 创建数组
s = np.array([1,2,3,4])
a = np.array([[1,2,3],[4,5,6],[7,8,9]])

# shape 获得数组大小
print (s.shape)
print (a.shape)

# dtype 获得元素属性
print (s.dtype)

# 修改b数组九宫格中间元素
a[1,1] = 10
print (a)


# ### 2 结构数组
# 
# C语言中通过struct定义结构类型，结构中的字段占据连续的内存空间，每个结构体占用的内存大小都相同。
# 
# 在NumPy中：

# In[6]:


import numpy as np

# dtype定义结构类型
# S:(byte-)字符串, i:(有符号)整型，f:浮点型
persontype = np.dtype({
    'names':['name','age','chinese','math','english'],
    'formats':['S32','i','i','i','f']
})

# array中指定结构数组的类型 dtype = persontype 
peoples = np.array([("ZhangFei",32,75,100,90),("GuanYu",24,85,96,88.5),
                    ("ZhaoYun",28,85,92,96.5),("HuangZhong",29,65,85,100)],
                  dtype = persontype)

# 打印每个人的年龄
ages = peoples[:]['age']
print (ages)

# 计算平均年龄
print (np.mean(ages))


# ## ufunc (universal function object) 处理数组的函数
# 
# ### 1 创建连续数组

# In[10]:


# 创建等差数组的两种方式

# arange 类似range(初始值，终值，步长)，默认不包含终值
x1 = np.arange(1,11,2)

# linspace 线性等分向量 linear space，(初始值，终值，元素个数)，默认包含终值
# 默认得到的为浮点型，用dtype定义其为整型
x2 = np.linspace(1,9,5,dtype=int)

print (x1)
print (x2)


# ### 2 算数运算

# In[13]:


# 加减乘除
print (np.add(x1,x2))
print (np.subtract(x1,x2))
print (np.multiply(x1,x2))
print (np.divide(x1,x2))

# n次方：x1为基数，x2为次数
print (np.power(x1,x2))

# 取余两种方式：remainder 或 mod 
print (np.remainder(x1,x2))
print (np.mod(x1,x2))


# ### 3 统计函数

# In[22]:


# 统计最值
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])

# 最大值 amax()
print (np.amax(a))

# axis=0 轴 纵向：[1,4,7],[2,5,8],[3,6,9]每个的最大值
print (np.amax(a,0))

# axis=1 轴 横向：[1,2,3],[4,5,6],[7,8,9]每个的最大值
print (np.amax(a,1))

# 最小值 amin()
print (np.amin(a))
print (np.amin(a,0))
print (np.amin(a,1))


# In[16]:


# 统计最大值与最小值之差

print (np.ptp(a))
print (np.ptp(a,0))
print (np.ptp(a,1))


# In[23]:


# 统计数组的百分位数

print (np.percentile(a,50))
print (np.percentile(a,50, axis = 0))
print (np.percentile(a,50, axis = 1))


# In[24]:


# 统计中位数

print (np.median(a))
print (np.median(a, axis = 0))
print (np.median(a, axis = 1))

# 统计平均数
print (np.mean(a))
print (np.mean(a, axis = 0))
print (np.mean(a, axis = 1))


# In[28]:


# 统计加权平均值

s = np.array([1,2,3,4])

# 默认情况下，权重相同
print (np.average(s))

# 指定权重数组
wts = np.array([1,2,3,4])
print (np.average(s, weights = wts))


# In[30]:


# 统计标准差
print (np.std(s))

# 统计方差
print (np.var(s))


# ### 4 排序

# In[32]:


# NumPy 排序
# sort(a, axis = -1, kind = 'quicksort', order = None)
# 默认为快速排序 quicksort
# 还可以选择合并排序 mergesort，堆排序 heapsort
# axis 默认是 -1，即沿着数组的最后一个轴排序
# axis = None 表示所有元素作为一个向量进行排序
# order 对于结构数组，指定按照某个字段排序

p = np.array([[4,3,2],[2,4,1]])
print (np.sort(p))
print (np.sort(p, axis = None))
print (np.sort(p, axis = 0))
print (np.sort(p, axis = 1))


# ## 练习：统计全班成绩
# 
# 假设团队5名学员，成绩如下表。统计各科目平均成绩、最小最大成绩、方差、标准差，然后按总成绩排序，得出名次进行成绩输出。
# 
# |姓名|语文|英语|数学|
# |:--:|:--:|:--:|:--:|
# |张飞|66|65|30|
# |关羽|95|85|98|
# |赵云|93|92|96|
# |黄忠|90|88|77|
# |典韦|80|90|90|
# 
# ### 我的解答

# In[124]:


# 我的解答

# -*- coding: utf-8 -*-
import numpy as np

persontype = np.dtype({
    'names':['name','chinese','english','math','total'],
    'formats':['S32','i','i','i','i']
})

peoples = np.array([("Zhangfei",66,65,30,0),("Guanyu",95,85,98,0),
                    ("Zhaoyun",93,92,96,0),("Huangzhong",90,88,77,0),
                    ("Dianwei",80,90,90,0)],
                  dtype = persontype)

chineses = peoples[:]['chinese']
englishes = peoples[:]['english']
maths = peoples[:]['math']

# 计算每个人总分
peoples[:]['total'] = chineses + englishes + maths
totals = peoples[:]['total']

# table 在原始列表上加了总分
table = np.array([chineses,englishes,maths,totals])

# 包含所有统计数据的数组
stat = np.array([np.mean(table, axis = 1),np.amax(table, axis = 1),
                 np.amin(table, axis = 1),np.var(table, axis = 1),
                np.std(table, axis = 1)])

# 统计名称列向量
statnames = np.array([["平均分:"],["最高分:"],["最低分:"],["方 差:"],["标准差:"]])

# 打印首行
print ("   统计值    语文    英语   数学   总分")

# 合并统计名称列向量和统计值矩阵
# 这个方法把所有元素都变成字符串了，如何让数值仍然保持浮点型呢？
print (np.hstack((statnames,np.round(stat, decimals = 1))))

# 排序，默认是从小到大，如何从大到小排呢？
print ("按总成绩从低到高排序如下：")
print (np.sort(peoples, order = 'total'))


# In[123]:


# 试下用循环来输出统计值
print ("   统计值   语文  英语   数学")
j = 0
while j < 5:
    i = -1
    while i < 3:
        if i < 0:
            print ("%s" %(statnames[j]), end = " ")
            i += 1
        else:
            print ("%.1f" %(stat[j,i]), end = "  ")
            i += 1
    print ('\n')
    j += 1


# ### 待解决疑问
# 
# - 在输出统计值时，我通过合并统计名称列向量和统计值矩阵，得到最后的大矩阵，但这个方法把所有元素都变成字符串类型，如何让数值仍然保持浮点型呢？
# 
# - sort 排序，默认是从小到大，如何从大到小排呢？
# 
# - 我的解法感觉并不精简，若有大神路过此地，可否指点一二？Thanks.
# 
# ## 参考资料
# 
# [1] 极客时间-数据分析实战第4讲
# 
# [2] [NumPy教程](http://www.runoob.com/numpy/numpy-tutorial.html)
