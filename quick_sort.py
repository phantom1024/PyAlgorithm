# -*- coding: UTF-8 -*-
# @File     : quick_sort.py
# @Author   : phantom
# @Date     : 2018/1/23
# @PyVersion: python 3
# @Software : PyCharm Community Edition 
# @Des      : 快速排序算法
"""
1.分而治之策略（divide and conquer，D&C）:一种著名的递归式问题解决方法
用D&C解决问题的过程有两个步骤：
（1）找出基线条件，条件必须尽可能简单
（2）不断将问题分解（缩小规模），直到符合基线条件

快速排序其实就是一个D&C算法

2.基本流程：
（1）选择基准值
（2）将数组分为两个子数组：小于基准值的元素和大于基准值的元素
（3）对这两个子数组进行快速排序（递归）

3.条件列表解析：[i for i in arr[1:] if i <= pivot]
等价于：
new_arr = []
for item in arr[1:]:
    if item <= pivot:
        new_arr.append(item)

"""

def quick_sort(arr):
    if len(arr) < 2:  # 基线条件：只有一个元素或为空
        return arr
    else:
        pivot = arr[0]  # 基准值
        less = [i for i in arr[1:] if i <= pivot]  # 由所有小于基准值的元素组成的子数组
        more = [i for i in arr[1:] if i > pivot]  # 由所有大于基准值的元素组成的子数组
        return quick_sort(less) + [pivot] + quick_sort(more)

print(quick_sort([10, 7, 5, 15, 1]))
