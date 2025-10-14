from yijiang_tool import *


def companion_task():

	while True:
		# 移动到目标位置
		while True:
			x = random() * get_world_size() // 1
			y = random() * get_world_size() // 1

			move_to(x, y)

			if get_entity_type() == None:
				break

		plant_stack = []

		plant_entity(Entities.Carrot, True)

		plant_stack.append((get_pos_x(), get_pos_y()))

		for _ in range(max_drones()):
			companion = get_companion()
			
			if companion == None:
				break

			move_to(companion[1][0], companion[1][1])

			if get_entity_type() != None:
				break

			plant_entity(companion[0], True)
			plant_stack.append(companion[1])

		# 回归收获
		while plant_stack:
			x, y = plant_stack.pop()
			move_to(x, y)

			while not can_harvest():
				pass

			harvest()


def companion_task_v2():

	while True:
		x = random() * get_world_size() // 1
		y = random() * get_world_size() // 1

		move_to(x, y)

		if get_entity_type() == None:
			break

	while True:
		plant_entity(Entities.Carrot, True)

		# 获得半身
		companion = get_companion()

		if companion == None:
			break

		# 移动到半身位置
		move_to(companion[1][0], companion[1][1])

		# 如果有植物 就收获 改种
		if get_entity_type():
			while not can_harvest():
				use_item(Items.Fertilizer)
			harvest()

		# 种植
		plant_entity(companion[0], True)


def till_row():

	for _ in range(get_world_size()):
		till()
		move(East)


if __name__ == "__main__":
	clear()  # 初始化环境

	do_all(till_row)

	# 散无人机
	while spawn_drone(companion_task_v2) != None:
		pass
	companion_task_v2()
