from yijiang_tool import *

def get_size():
	# 无人机数量和世界大小的较小值
	if get_world_size() < max_drones():
		return get_world_size()
	else:
		return max_drones()


def scan_row():
	# 扫描这一行都有没有南瓜
	row_data = []
	for _ in range(get_world_size()):
		if get_entity_type() == Entities.Pumpkin:
			# 如果有
			row_data.append(True)
		else:
			# 如果没有
			row_data.append(False)
			# 补种
			plant_entity(Entities.Pumpkin, True)
		move(East)

	return row_data


def plant_pumkin_row():
	# 种植一排南瓜
	for _ in range(get_world_size()):
		plant_entity(Entities.Pumpkin, True)
		move(East)


def harvest_pumkin_row():
	# 采集一排南瓜
	for _ in range(get_world_size()):
		if get_entity_type() == Entities.Pumpkin:
			if can_harvest():
				harvest()
				plant_entity(Entities.Pumpkin, True)
		else:
			plant_entity(Entities.Pumpkin, True)

		move(East)


# 弃用
def pumpkin_row():
	
	plant_pumkin_row()
	return scan_row()

# 弃用
def get_max_rect(data):
	max_area = 0
	max_rect = None

	for i in range(len(data)):
		for j in range(len(data[i])):
			if data[i][j]:
				width = 1
				while j + width < len(data[i]) and data[i][j + width]:
					width += 1
				area = width * (i + 1)
				if area > max_area:
					max_area = area
					max_rect = (i, j, width, i + 1)

	return max_rect

def ensure_pumpkin_row():
	# 确保这一行有南瓜
	for _ in range(get_world_size()):
		while get_entity_type() != Entities.Pumpkin:
			plant_entity(Entities.Pumpkin, True)

			use_item(Items.Fertilizer, 2)

		move(East)


def main():
	clear()

	drone_list = []
	pumpkin_data = []

	for _ in range(get_size() - 1):
		if num_drones() < get_size():
			drone_list.append(spawn_drone(pumpkin_row))

		move(North)
	
	last_row = pumpkin_row()
	
	# 获取子无人机数据
	for drone in drone_list:
		pumpkin_data.append(wait_for(drone))
	pumpkin_data.append(last_row)

	quick_print(pumpkin_data)


def do_all(function):
	drone_list = []
	move_to(0, 0)

	for _ in range(get_size() - 1):
		if num_drones() < get_size():
			drone_list.append(spawn_drone(function))
		move(North)

	function()

if __name__ == "__main__":
	# main()
	clear()
	# 先中一整个
	# while(True):
	# 	for _ in range(2):
	# 		do_all(plant_pumkin_row)

	move_to(0, 0)
	harvest()
	while True:
		do_all(plant_pumkin_row)
		do_all(ensure_pumpkin_row)

		harvest()
