# 种植作物
def plant_entity(plant_entity, use_water=False, water_below=0.7):

	# 洒水逻辑：当启用浇水且当前水位低于阈值时
	if use_water and get_water() < water_below:
		use_item(Items.Water)

	# 作物类型不匹配时重新种植
	if get_entity_type() != plant_entity:
		# 胡萝卜和南瓜需要松土条件
		if plant_entity in (Entities.Carrot, Entities.Pumpkin, Entities.Sunflower, Entities.Cactus):
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


def get_size():
	# 无人机数量和世界大小的较小值
	if get_world_size() < max_drones():
		return get_world_size()
	else:
		return max_drones()


def plant_entity_row(entity, use_water=False, water_below=0.7):
	# 先种植一排南瓜
	for _ in range(get_world_size()):
		plant_entity(entity, use_water, water_below)
		move(East)


def do_all(function, dir=North):

    # 存储所有子无人机的引用
    drone_list = []
    # 存储所有执行结果
    result = []

    # 移动至初始位置(0, 0)
    move_to(0, 0)

    # 当无人机数量不足时创建新无人机
    for _ in range(get_world_size() - 1):
        if num_drones() < get_size():
            drone_list.append(spawn_drone(function))
        else:
            for drone in drone_list:
                wait_for(drone)

            drone_list.append(spawn_drone(function))

        move(dir)

    # 主无人机最后一行执行任务
    last_result = function()

    # 获得子无人机返回值
    for drone in drone_list:
        result.append(wait_for(drone))
    # 合并自己的返回值
    result.append(last_result)

    return result

def list_reverse(arr):
	return arr[::-1]
