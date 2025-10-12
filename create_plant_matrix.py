# 创建二维植物矩阵，维度与世界大小相同
plant_matrix = []

# 遍历Y轴坐标
for y in range(get_world_size()):
    row_list = []  # 当前行的植物列表

    # 遍历X轴坐标
    for x in range(get_world_size()):

        # 下半部分区域（Y轴中点及以下）
        if y >= get_world_size() // 2:
            # 右下四分之一区域种植南瓜
            if x >= get_world_size() // 2:
                row_list.append(Entities.Pumpkin)
            # 左下四分之一区域种植胡萝卜
            else:
                row_list.append(Entities.Carrot)

        # 上半部分区域
        else:
            # 棋盘格模式交替种植树木和草地
            if (x + y) % 2 == 0:
                row_list.append(Entities.Tree)  # 偶数位置种植树木
            else:
                row_list.append(Entities.Grass)  # 奇数位置种植草地

    plant_matrix.append(row_list)

print(plant_matrix)
