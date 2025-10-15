from yijiang_tool import *

if __name__ == "__main__":
	clear()

	# def test():
	# 	result = []

	# 	for _ in range(get_world_size()):
	# 		plant_entity(Entities.Carrot, True)
	# 		result.append((get_pos_x(), get_pos_y()))
	# 		move(East)

	# 	return result

	# result = do_all(test)

	# for row in result:
	# 	quick_print(row)

	list = [(0, 0)]
	drone_list = []

	for i in range(5):

		def test_thread_ref():
			move_to(i + 3, i + 3)
			list.append((get_pos_x(), get_pos_y()))

		drone_list.append(spawn_drone(test_thread_ref))

	for drone in drone_list:
		wait_for(drone)
	quick_print(list)