from yijiang_tool import *

def creat_maze():
	plant(Entities.Bush)
	substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)


def dfs_solve_maze():
	start_x, start_y = get_pos_x(), get_pos_y()

	stack = [(start_x, start_y, None)]  #(x, y, 往哪走)
	visited = set()
	visited.add((start_x, start_y))
	path = [(start_x, start_y, None)]  # 实际移动的路径

	while stack:

		x, y, move_dir = stack.pop()
		# quick_print(visited, stack, x, y, move_dir)

		# 执行移动（如果是第一次访问该位置）
		if move_dir:
			move(move_dir)
			path.append((get_pos_x(), get_pos_y(), move_dir))
			visited.add((get_pos_x(), get_pos_y()))

		# 检查是否到达终点
		if get_entity_type() == Entities.Treasure:
			return True

		# 尝试所有可能的方向
		found_move = False
		for direction in [North, South, East, West]:
			if can_move(direction):
				# 计算新位置
				new_x, new_y = get_pos_x(), get_pos_y()
				if direction == North:
					new_y += 1
				elif direction == South:
					new_y -= 1
				elif direction == East:
					new_x += 1
				elif direction == West:
					new_x -= 1

				if (new_x, new_y) not in visited:
					stack.append((get_pos_x(), get_pos_y(), direction))
					found_move = True

		# 如果没有找到可移动的方向，回溯
		if not found_move and path:
			# 移除直到和stack中下一个的起始位置一样
			while path and (get_pos_x(), get_pos_y()) != (stack[-1][0], stack[-1][1]):
				last_path = path.pop()
				move(get_opposite_dir(last_path[2]))

	return False


def a_star_solve_maze():
	# 获取起点和目标位置
	start_x, start_y = get_pos_x(), get_pos_y()
	target_x, target_y = measure()  # 获取宝藏坐标

	heap = []
	heap.append(
		{
			"f": 0,
			"g": 0,
			"h": 0,
			"pos": (start_x, start_y),
			"path": [(start_x, start_y)],
		}
	)
	closed_set = set()
	pre_pos_list = [(start_x, start_y)]

	while heap:
		# 找f最小的
		minf = heap[0]["f"]
		minf_index = 0
		for i in range(len(heap)):
			if heap[i]["f"] < minf:
				minf = heap[i]["f"]
				minf_index = i

		# pop out
		cur_node = heap.pop(minf_index)

		# 检查是否已访问
		if cur_node["pos"] in closed_set:
			continue

		# 检查是否到达终点
		if cur_node["pos"] == (target_x, target_y):
			return cur_node["path"]

		quick_print(pre_pos_list)
		quick_print(cur_node)
		# 移动过去
		for pre_pos in pre_pos_list[::-1]:
			quick_print((get_pos_x(), get_pos_y()), pre_pos)
			move_to_tuple(pre_pos)
			if pre_pos in cur_node["path"]:
				break

		flag = False
		for pos in cur_node["path"]:
			if pos == (get_pos_x(), get_pos_y()):
				flag = True
			if flag:
				quick_print((get_pos_x(), get_pos_y()), pos)
				move_to_tuple(pos)

		pre_pos_list = cur_node["path"]
		closed_set.add(cur_node["pos"])

		# 扩展当前节点
		for direction in [North, South, East, West]:
			if can_move(direction):
				# 计算新位置
				new_x, new_y = cur_node["pos"][0], cur_node["pos"][1]
				if direction == North:
					new_y += 1
				elif direction == South:
					new_y -= 1
				elif direction == East:
					new_x += 1
				elif direction == West:
					new_x -= 1

				# 检查是否已访问
				if (new_x, new_y) in closed_set:
					continue

				# 计算新的成本
				new_g = cur_node["g"] + 1
				new_h = abs(new_x - target_x) + abs(new_y - target_y)
				new_f = new_g + new_h

				# 添加到堆中
				heap.append(
					{
						"f": new_f,
						"g": new_g,
						"h": new_h,
						"pos": (new_x, new_y),
						"path": cur_node["path"] + [(new_x, new_y)],
					}
				)


def get_opposite_dir(dir):
	if dir == North:
		return South
	elif dir == South:
		return North
	elif dir == East:
		return West
	elif dir == West:
		return East
	return None

def main_299_challenge():
	clear()
	plant(Entities.Bush)

	for i in range(299):
		substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)
		dfs_solve_maze()

	harvest()

def main():
	clear()
	while True:
		creat_maze()
		a_star_solve_maze()
		harvest()

if __name__ == "__main__":
<<<<<<< HEAD
	main_299_challenge()
=======
	# main_299_challenge()
	# main()

	clear()
	creat_maze()
	print(a_star_solve_maze())
>>>>>>> 506babe0f4507a0701bd5a4784ea83acd9625521
