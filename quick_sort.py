#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author  : shengxd
@Contact : 740693424@qq.com
@File    :   quick_sort.py
@Time    :   2019/8/7 10:38
@Desc    :

"""
# 选择排序：
# 比如在一个长度为N的无序数组中，在第一趟遍历N个数据，找出其中最小的数值与第一个元素交换，
#                              第二趟遍历剩下的N-1个数据，找出其中最小的数值与第二个元素交换......
#                              第N-1趟遍历剩下的2个数据，找出其中最小的数值与第N-1个元素交换，
# 至此选择排序完成


def quick_sort(my_list):
    """
    选择排序
    :param my_list: 要排序的列表
    :return:
    """
    len_my_list = len(my_list)
    for i in range(len_my_list):
        min_value = my_list[i]
        min_index = i
        # 找出最小值
        for j in range(i+1, len_my_list):
            if my_list[j] < min_value:
                min_value = my_list[j]
                min_index = j
        # 交换数值
        my_list[i], my_list[min_index] = min_value, my_list[i]

    return my_list


if __name__ == "__main__":
    my_list = [9, 7, 2, 3, 8, 1, 5, 10]
    quick_sort(my_list)
    print(my_list)


