from yijiang_tool import *

# 种植一行仙人掌
def plant_cactus_row():
	for _ in range(get_world_size()):
		plant_entity(Entities.Cactus, True)
		move(East)


def bubble_sort(dir):
    # 冒泡排序
    start_x = get_pos_x()
    start_y = get_pos_y()

    for i in range(get_world_size() - 1):
        for j in range(get_world_size() - 1 - i):
			
			# 获取大小
            cur_value = measure()
            east_value = measure(dir)

			# 比较大小并且交换
            if cur_value > east_value:
                swap(dir)

            move(dir)

        # 回到起点
        move_to(start_x, start_y)


if __name__ == "__main__":
	harvest()
	clear()

	while True:
		# 种仙人掌
		do_all(plant_cactus_row)

		# 排序 row
		def row_sort_task():
			bubble_sort(East)
		do_all(row_sort_task)

		# 排序 col
		def col_sort_task():
			bubble_sort(North)
		do_all(col_sort_task, East)

		harvest()

