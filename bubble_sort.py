#!/usr/bin/env python
# -*- encoding: utf-8 -*-


def bubble_sort(mylist):
    len_mylist = len(mylist)
    num_of_compare_round = 0
    sort_complete_num = 0
    for i in range(len_mylist):
        num_of_compare_round2 = 0
        for j in range(len_mylist-i-1):
            num_of_compare_round2 += 1
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
            else:
                sort_complete_num += 1
        num_of_compare_round += num_of_compare_round2
        if sort_complete_num == len_mylist-i-1:
            print("sort has completed")
            break
    print("num_of_compare_round {}".format(num_of_compare_round))
    return mylist


if __name__ == "__main__":
    mylist = [9, 3, 1, 4, 2, 7, 8, 6, 5]
    mylist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    mylist1 = bubble_sort(mylist1)
    print(mylist1)

