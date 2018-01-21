# -*- coding: UTF-8 -*-
# @File     : binary_search.py
# @Author   : phantom
# @Date     : 2018/1/21
# @PyVersion: python 3
# @Software : PyCharm Community Edition 
# @Des      : 二分查找算法，算法复杂度：O(logn)
"""
算法描述：
（1）起始下标low，末尾下标high
（2）若low<=high，则（3）；否则返回null
（3）low和high的中间位置mid，根据mid取到中间元素，若中间元素与查找目标相等，则返回mid，若不相等则（4）
（4）若中间元素大于查找目标，则：high = mid - 1，然后回到（2）；否则（5）
（5）若中间元素小于查找目标，则：low = mid + 1，然后回到（2）
"""

# list : 搜索列表；item：被搜索的元素
# tips : python3和2的不同点，/ 会带小数， // 无论是否整除返回的都是int，而且是去尾整除
def binary_search(list, item):
    low = 0  # list的起始下标
    high = len(list) - 1  # list的末尾下标
    while low <= high:  # 范围还未缩小到只剩1个元素
        mid = (low + high) // 2  # 每次搜索范围的中间位置下标
        guess = list[mid]  # 每次搜索范围中间元素的值
        if guess == item:  # 找到目标，返回目标的下标
            return mid
        if guess > item:  # 若猜的数字大于目标数字
            high = mid - 1  # 右指针的下标变为中间下标的左边一个
        else:  # 若猜的数字小于等于目标数字
            low = mid + 1  # 左指针的下标变为中间下标的右边一个
    return None  # 未找到指定元素

# Test code
a_list = [1, 3, 5, 7, 9]
print(binary_search(a_list, 3))  # 正确结果应该为1
print(binary_search(a_list, -1))  # 正确结果应该为None


