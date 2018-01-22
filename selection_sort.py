# -*- coding: UTF-8 -*-
# @File     : selection_sort.py
# @Author   : phantom
# @Date     : 2018/1/22
# @PyVersion: python 3
# @Software : PyCharm Community Edition 
# @Des      : 选择排序算法，算法时间：O(n x n),实际为n x 1/2 x n，但大O表示法省略如1/2这样的常数
#             n,n-1,n-2,...,2,1

# 从数组中找出最小值的方法
def findSmallest(arr):
    smallest = arr[0]  # 存储最小的值，初始默认为数组第一个元素
    smallest_index = 0  # 存储最小值的索引，初始默认为0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# 选择排序方法
def selectionSort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)  # 找到当前arr中最小元素的索引
        new_arr.append(arr.pop(smallest_index))  # 新数组添加元素的同时，被排序数组最小元素出栈
    return new_arr

# Test code
print(selectionSort([5, 3, 6, 2, 10]))  # 正确结果：[2,3,5,6,10]
