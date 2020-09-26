# Import thư viện numpy
import numpy as np

""" Boolean Indexing """

# Sử dụng hàm array trong thư viện numpy để tạo mảng các tên (names) với dữ liệu có có thể bị trùng
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# Sử dụng hàm randn trong numpy.random để tạo mảng 2 chiều (data) kích thước 7x4 với dữ liệu ngẫu nhiên
data = np.random.randn(7,4)
# In ra mảng names
print(names)
# In ra mảng data
print(data)
# In ra mảng trả về giá trị True/False khi so sánh từng phần tử của mảng names với 'Bob'
# True khi names[i] = 'Bob' và ngược lại
print(names == 'Bob')
# In ra các dòng của mảng data tương ứng với chỉ số mà tại đó mảng names trả về True khi so sánh bằng với 'Bob'
print(data[names == 'Bob'])
# Tương tự dòng trên, nhưng chỉ lấy cột có chỉ số từ 2 trở lên
print(data[names == 'Bob', 2:])
# Tương tự dòng trên, nhưng chỉ lấy cột có chỉ số là 3
print(data[names == 'Bob', 3])
# In ra mảng trả về giá trị True/False khi so sánh từng phần tử của mảng names với 'Bob'
# False khi names[i] = 'Bob' và ngược lại
print(names != 'Bob')
# 
print(data[~(names == 'Bob')])
mask = (names == 'Bob') | (names == 'Will')
print(mask)
print(data[mask])
data[data<0] = 0
print(data)
data[names != 'Joe'] = 7
print(data)

""" Expressing Conditional Logic as Array Operations """

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
print(result)
result = np.where(cond, xarr, yarr)
print(result)
arr = np.random.randn(4,4)
print(arr)
print(np.where(arr > 0, 2, -2))
print(np.where(arr > 0, 2, arr)) # set only positive values to 2
result = []
n = 5
cond1 = np.array([True, False, True, True, False])
cond2 = np.array([True, False, False, True, True])
for i in range(n):
    if cond1[i] and cond2[i]:
        result.append(0)
    elif cond1[i]:
        result.append(1)
    elif cond2[i]:
        result.append(2)
    else:
        result.append(3)

print(result)
print(np.where(cond1 & cond2, 0, np.where(cond1, 1, np.where(cond2, 2, 3))))
result = 1 * cond1 + 2 * cond2 + 3 * ~(cond1 | cond2)
print(result)
