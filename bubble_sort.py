#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 冒泡排序


def bubble_sort(my_list):
    """
    升序
    :param my_list: 传入要排序的列表
    :return:
    """
    len_my_list = len(my_list)
    num_of_compare_round = 0  # 统计比较的总次数
    sort_complete_num = 0     # 优化冒泡排序的判断条件：当比较完一轮，发现已排好序，不再进行下一轮比较
    for i in range(len_my_list):
        num_of_compare_round2 = 0
        for j in range(len_my_list-i-1):
            num_of_compare_round2 += 1
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
            else:
                sort_complete_num += 1
        num_of_compare_round += num_of_compare_round2
        if sort_complete_num == len_my_list-i-1:
            print("sort has completed")
            break
    print("num_of_compare_round {}".format(num_of_compare_round))
    return my_list


if __name__ == "__main__":
    my_list = [9, 3, 1, 4, 2, 7, 8, 6, 5]
    my_list = bubble_sort(my_list)
    print(my_list)
    my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_list1 = bubble_sort(my_list1)
    print(my_list1)

