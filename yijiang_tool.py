# 种植作物
def plant_entity(plant_entity, use_water=False, water_below=0.7):

    # 洒水逻辑：当启用浇水且当前水位低于阈值时
    if use_water and get_water() < water_below:
        use_item(Items.Water)

    # 作物类型不匹配时重新种植
    if get_entity_type() != plant_entity:
        # 胡萝卜和南瓜需要松土条件
        if plant_entity in (Entities.Carrot, Entities.Pumpkin):
            # 检查当前地块是否为可种植的土壤
            if get_ground_type() != Grounds.Soil:
                till()  # 松土操作

        # 种植目标作物
        plant(plant_entity)


# 移动到指定坐标
def move_to(x, y):
    current_x, current_y = get_pos_x(), get_pos_y()
    size = get_world_size()

    # X轴最短路径计算
    dx = (x - current_x) % size
    if dx > size // 2:
        move_dir_x = West
        steps_x = size - dx
    else:
        move_dir_x = East
        steps_x = dx

    # Y轴最短路径计算
    dy = (y - current_y) % size
    if dy > size // 2:
        move_dir_y = South
        steps_y = size - dy
    else:
        move_dir_y = North
        steps_y = dy

    # 执行移动
    for _ in range(steps_x):
        move(move_dir_x)
    for _ in range(steps_y):
        move(move_dir_y)
