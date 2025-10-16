from yijiang_tool import *
from create_plant_matrix import create_plant_single_entity_matrix

# 只负责种植需求植物的 伴生植物来提高产量
# 每个无人机负责一行, 一直种需求植物并读取伴生植物
# 并且持续读取 伴生植物, 如果有则, 过去尝试种植, 如果种植位置是
def plant_single_entity_with_companion(entity_type):
	
	for _ in range(get_world_size()):
		cur_x = get_pos_x()
		cur_y = get_pos_y()

		# 种植需求植物
		if get_entity_type() == None:
			plant_entity(entity_type, True)

		# 读取伴生植物
		if get_entity_type() == entity_type:
			companion = get_companion()

			if companion:
				# 尝试种植伴生植物
				move_to(companion[1][0], companion[1][1])

				# 如果是需求植物, 或者是 None, 则尝试种植伴生植物
				if get_entity_type() == None or get_entity_type() == entity_type:
					harvest()
					plant_entity(companion[0], True)

		# 返回并且向 East 移动一个
		move_to((cur_x + 1) % get_world_size(), cur_y)


def plant_single_entity_with_companion_v2(entity_type):
	# 全种需求植物, 并且拿到一个总植物和伴生植物表
	# 拿到需求植物和伴生植物表, 遍历一遍之后 往一个矩阵里面记录
	# 矩阵记录 植物位置 和 伴生植物位置 (或者直接用列表)
	# 还有一个列表记录需要执行的对
	#
	# 每个无人机负责一行, 如果有对应需要种植的就去种植并且回来收获, 再把两边都补种, 并且记录在总伴生列表种
	#

	total_companion_pool_dict = {}

	def first_plant_task():
		result = {}

		for _ in range(get_world_size()):
			plant_entity(entity_type, True)
			companion = get_companion()
			if companion:
				comp_entity_type, comp_pos = companion
				result[(get_pos_x(), get_pos_y())] = (comp_pos, comp_entity_type)

			move(East)

		return result

	result = do_all(first_plant_task)

	while True:

		# 转换格式
		for row in result:
			for key in row:
				total_companion_pool_dict[key] = row[key]

		quick_print(len(total_companion_pool_dict))

		record_pos_set = set()
		delete_pos_set = set()	
		record_companion_dict = {}

		for pos in total_companion_pool_dict:
			comp_pos, comp_entity_type = total_companion_pool_dict[pos]

			if comp_pos not in record_pos_set and pos not in record_pos_set:
				# 两个都不在 说明可以记录
				record_pos_set.add(comp_pos)
				record_pos_set.add(pos)

				record_companion_dict[pos] = (comp_pos, comp_entity_type)

				# 并且记录删除因为伴生植物占据的 主植物 还有自己
				delete_pos_set.add(comp_pos)
				delete_pos_set.add(pos)

		# 删除
		for pos in delete_pos_set:
			total_companion_pool_dict.pop(pos)

		quick_print(len(total_companion_pool_dict))
		quick_print(len(record_companion_dict))

		def second_plant_task():
			result = {}

			for _ in range(get_world_size()):
				if (get_pos_x(), get_pos_y()) in record_companion_dict:
					cur_pos = (get_pos_x(), get_pos_y())
					# 说明是需要种植的
					comp_pos, comp_entity_type = record_companion_dict[cur_pos]

					# 过去尝试种植
					move_to_tuple(comp_pos)
					harvest()
					plant_entity(comp_entity_type, True)

					# 回来收获
					move_to_tuple(cur_pos)
					harvest()

					# 补种
					plant_entity(entity_type, True)

					# 记录
					companion = get_companion()
					if companion:
						temp_comp_entity_type, temp_comp_pos = companion
						result[(get_pos_x(), get_pos_y())] = (
							temp_comp_pos,
							temp_comp_entity_type,
						)

					# 移动到刚刚那个的伴生位置
					move_to_tuple(comp_pos)
					harvest()

					# 补种
					plant_entity(entity_type, True)

					# 记录
					companion = get_companion()
					if companion:
						temp_comp_entity_type, temp_comp_pos = companion
						result[(get_pos_x(), get_pos_y())] = (
							temp_comp_pos,
							temp_comp_entity_type,
						)

					# 完工去下一位置
					move_to((cur_pos[0] + 1) % get_world_size(), cur_pos[1])

				else:
					move(East)

			return result

		result = do_all(second_plant_task)


def plant_single_entity_with_companion_v3(entity_type):

	def first():
		plant_entity_row(entity_type, True)

	do_all(first)

	def second():
		while True:

			companion = get_companion()
			if get_entity_type() == entity_type and companion:

				cur_pos = (get_pos_x(), get_pos_y())
				comp_entity_type, comp_pos = companion

				# 过去尝试种植
				move_to_tuple(comp_pos)
				harvest()
				plant_entity(comp_entity_type, True)
				# 回来收获
				move_to_tuple(cur_pos)
				harvest()
				# 补种
				plant_entity(entity_type, True)
				# 移动到刚刚那个的伴生位置
				move_to_tuple(comp_pos)
				harvest()
				# 补种
				plant_entity(entity_type, True)
				# 完工去下一位置
				move_to((cur_pos[0] + 1) % get_world_size(), cur_pos[1])
			else:
				move(East)

	do_all(second)


def plant_single_entity_with_companion_v4(entity_type):

	plant_matrix = create_plant_single_entity_matrix(entity_type)

	def first():
		plant_entity_with_dict(plant_matrix, True)

	do_all(first)

	# pos_list = [
	# 	(0, 0),
	# 	(30, 2),
	# 	(0, 28),
	# 	(3, 4),
	# 	(26, 31),
	# 	(5, 29),
	# 	(30, 7),
	# 	(29, 25),
	# 	(8, 3),
	# 	(24, 3),
	# 	(4, 24),
	# 	(3, 9),
	# 	(24, 27),
	# 	(10, 30),
	# 	(26, 9),
	# 	(31, 21),
	# 	(9, 7),
	# 	(20, 0),
	# 	(9, 24),
	# 	(31, 12),
	# 	(24, 22),
	# 	(13, 2),
	# 	(21, 8),
	# 	(3, 19),
	# 	(7, 12),
	# 	(19, 28),
	# 	(13, 26),
	# 	(26, 14),
	# 	(27, 18),
	# 	(13, 7),
	# 	(17, 4),
	# 	(9, 19),
	# ]

	pos_list = [
		(0, 0),
		(1, 3),
		(2, 6),
		(3, 9),
		(4, 12),
		(5, 15),
		(6, 18),
		(7, 21),
		(8, 24),
		(9, 27),
		(10, 30),
		(11, 1),
		(12, 4),
		(13, 7),
		(14, 10),
		(15, 13),
		(16, 16),
		(17, 19),
		(18, 22),
		(19, 25),
		(20, 28),
		(21, 31),
		(22, 2),
		(23, 5),
		(24, 8),
		(25, 11),
		(26, 14),
		(27, 17),
		(28, 20),
		(29, 23),
		(30, 26),
		(31, 29)
	]

	def second():
		while True:

			companion = get_companion()
			if get_entity_type() == entity_type and companion:

				cur_pos = (get_pos_x(), get_pos_y())
				comp_entity_type, comp_pos = companion

				# 过去尝试种植
				move_to_tuple(comp_pos)
				harvest()
				plant_entity(comp_entity_type, True)
				# 回来收获
				move_to_tuple(cur_pos)
				harvest()
				# 补种
				plant_entity(plant_matrix[(get_pos_x(), get_pos_y())], True)
				# 移动到刚刚那个的伴生位置
				move_to_tuple(comp_pos)
				harvest()
				# 补种
				plant_entity(plant_matrix[(get_pos_x(), get_pos_y())], True)
				# 完工去下一位置
				move_to((cur_pos[0] + 1) % get_world_size(), cur_pos[1])
			else:
				move(East)

	for i in range(len(pos_list) - 1):

		def task():
			move_to_tuple(pos_list[i])

			for _ in range(15000):
				pass

			second()

		spawn_drone(task)

	i += 1
	task()


def main_v1(entity_type):
	clear()

	do_all(till_row)

	while True:
		def task():
			plant_single_entity_with_companion(Entities.Carrot)
		do_all(task)
		do_all(harvest_row)


def main_v2(entity_type):
	clear()

	do_all(till_row)

	plant_single_entity_with_companion_v2(entity_type)


def main_v3(entity_type):
	clear()

	do_all(till_row)

	plant_single_entity_with_companion_v3(entity_type)


def main_v4(entity_type):
	clear()

	do_all(till_row)

	plant_single_entity_with_companion_v4(entity_type)


if __name__ == '__main__':
	
	# 可以做三个成就 胡萝卜, 木材, 草, 只要改种植的实体类型
	main_v4(Entities.Tree)
