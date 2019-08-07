#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author  : shengxd
@Contact : 740693424@qq.com
@File    :   insert_sort.py
@Time    :   2019/8/7 14:44
@Desc    :

"""
# 插入排序：插入即表示将一个新的数据插入到一个有序数组中，并继续保持有序。
# 例如有一个长度为N的无序数组，进行N-1次的插入即能完成排序；
# 第一次，数组第1个数认为是有序的数组，将数组第二个元素插入仅有1个有序的数组中；
# 第二次，数组前两个元素组成有序的数组，将数组第三个元素插入由两个元素构成的有序数组中......
# 第N-1次，数组前N-1个元素组成有序的数组，将数组的第N个元素插入由N-1个元素构成的有序数组中，
# 则完成了整个插入排序。
# ---------------------


def insert_sort(my_list):
    """
    插入排序
    :param my_list: 要排序的列表
    :return:
    """
    len_list = len(my_list)
    # 从第二个元素开始
    for i in range(1, len_list):
        insert_value = my_list[i]  # 取出当前元素与之前的有序元素进行比较
        current_insert_index = 0
        for j in range(i):   # 遍历之前的有序元素集合
            if insert_value < my_list[j]:  # 如果当前取出的元素比有序元素中的第j个元素小，保存当前位置的索引
                current_insert_index = j
                break
        # 把insert_value插入当前位置，其他有序元素依次后移（从后开始遍历元素）
        for m in range(i, current_insert_index, -1):
            my_list[m], my_list[m-1] = my_list[m-1], my_list[m]
        # my_list[current_insert_index] = insert_value
    return my_list


if __name__ == "__main__":
    mylist = [9, 7, 2, 8, 5, 6, 0]
    mylist = insert_sort(mylist)
    print(mylist)


