#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 冒泡排序


def bubble_sort(my_list):
    """

    :param my_list:
    :return:
    """
    len_my_list = len(my_list)
    num_of_compare_round = 0  # 统计比较的总次数
    sort_complete_num = 0     # 优化冒泡排序的判断条件：当比较完一轮，发现已排好序，不再进行下一轮比较
    for i in range(len_my_list):
        num_of_compare_round2 = 0
        for j in range(len_my_list-i-1):
            num_of_compare_round2 += 1
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
            else:
                sort_complete_num += 1
        num_of_compare_round += num_of_compare_round2
        if sort_complete_num == len_my_list-i-1:
            print("sort has completed")
            break
    print("num_of_compare_round {}".format(num_of_compare_round))
    return mylist


if __name__ == "__main__":
    mylist = [9, 3, 1, 4, 2, 7, 8, 6, 5]
    mylist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    mylist1 = bubble_sort(mylist1)
    print(mylist1)

