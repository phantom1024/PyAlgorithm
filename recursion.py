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
