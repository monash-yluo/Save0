from yijiang_tool import *


def plant_scan_sunflower_row():
	result = []

	for _ in range(get_world_size()):
		plant_entity(Entities.Sunflower, True)
		value = measure()
		result.append({"x": get_pos_x(), "y": get_pos_y(), "value": value})
		move(East)
		
	return result

def buket_sort(arr):
	# 找到最大值和最小值
	max_value = 15
	min_value = 7

	# 计算桶的数量
	bucket_count = max_value - min_value + 1
	# 创建空桶
	buckets = []
	for _ in range(bucket_count):
		buckets.append([])

	# 将元素分配到桶中
	for item in arr:
		index = item["value"] - min_value
		buckets[index].append(item)
		  
	return buckets


def one_loop(debug=False):
	# 执行分布式扫描任务
	result = do_all(plant_scan_sunflower_row)

	# 将多维结果展开为一维数组
	one_line_result = []
	for bucket in result:
		# 遍历每个子无人机返回的数据桶
		for item in bucket:
			one_line_result.append(item)

	# 对数据进行桶排序并逆序排列（从大到小）
	result = buket_sort(one_line_result)[::-1]

	# 调试输出排序结果
	if debug:
		for bucket in result:
			quick_print(bucket)

	# 多无人机协同收获流程
	drone_list = []
	for bucket in result:
		# 遍历每个排序后的数据桶
		for item in bucket:
			# 定义单个作物的收获任务
			def task():
				move_to(item["x"], item["y"])
				# 等待作物成熟
				while can_harvest() == False:
					pass

				# 调试输出当前位置和测量值
				if debug:
					quick_print("pos: ", get_pos_x(), get_pos_y(), "measure: ", measure())
				
				harvest()

			# 创建子无人机或主无人机执行任务
			drone = spawn_drone(task)
			if not drone:
				task()  # 主无人机直接执行
			else:
				drone_list.append(drone)

		# 等待当前桶内所有无人机完成
		for drone in drone_list:
			wait_for(drone)
		drone_list = []  # 重置无人机列表


def energy_row_only_15():
	for _ in range(get_world_size()):

		plant_entity(Entities.Sunflower, True)
		for _ in range(10):
			leaf = measure()

			if leaf == 15:
				break

			harvest()
			plant_entity(Entities.Sunflower, True)

		move(East)


def energy_row_haverst():
	for _ in range(get_world_size()):
		harvest()

		plant_entity(Entities.Sunflower, True)

		move(East)


if __name__ == "__main__":
	clear()

	while True:
		# one_loop(True)

		do_all(energy_row_only_15)
		do_all(energy_row_haverst)
