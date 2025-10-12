if __name__ == "__main__":

    x = 5

    # 测试if-elif-else语句
    if (x > 5):
        # 这行代码不会被执行 因为不大于5 (等于5)
        print("x is greater than 5")
    elif (x > 4):
        # 这行代码会被执行 因为大于4
        print("x is greater than 4")
    elif (x > 3):
        # 这行代码不会被执行 因为已经进入上一个elif 里面了
        print("x is greater than 3")
    else:
        # 这行代码不会被执行 因为已经进入上一个elif 里面了
        print("x is less than or equal to 3")

    list = [ 1, 2, 3, 4, 77, 10, 9 ]

    # 获得列表最大值的index
    max_index = list.index(max(list))
    print(max_index)

    # 获得列表最大值的index 通过foreach循环
    max_index = 0
    for i in range(len(list)):
        if list[i] > list[max_index]:
            max_index = i
    print(max_index)

    # 获得列表最大值的index 通过foreach循环
    max_index = 0
    for index, value in enumerate(list):
        if value > list[max_index]:
            max_index = index

    # 删除最大值
    del list[max_index]
    print(list)


    # 添加 9 到删除的位置
    list.insert(max_index, 9)
    print(list)
