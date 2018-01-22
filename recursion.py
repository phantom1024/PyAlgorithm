# -*- coding: UTF-8 -*-
# @File     : recursion.py
# @Author   : phantom
# @Date     : 2018/1/22
# @PyVersion: python 3
# @Software : PyCharm Community Edition 
# @Des      : 递归算法
"""
1.每个递归函数都有两部分组成：
（1）基线条件（base case）：函数不再调用自己的条件，避免形成无限循环
（2）递归条件（recursive case）：函数调用自己的条件
demo:
def count_down(i):
    print i
    if i <= 1:  # 基线条件
        return
    else:  # 递归条件
        count_down(i-1)
"""

# 递归在阶乘函数中的应用
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)
print(fact(5))  # 120

# 使用递归实现求和函数
def recursion_sum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    else:
        return arr.pop(0) + recursion_sum(arr)

print(recursion_sum([1, 2, 4, 7]))  # 14

# 使用递归计算列表包含的元素数
def recursion_count(arr):
    if len(arr) == 0:
        return 0
    else:
        arr.pop()
        return 1 + recursion_count(arr)

print(recursion_count([1, 2, 3, 4]))  # 4
