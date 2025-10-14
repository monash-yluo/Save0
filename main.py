from yijiang_tool import *

if __name__ == "__main__":
	clear()

	def test():
		result = []

		for _ in range(get_world_size()):
			plant_entity(Entities.Carrot, True)
			result.append((get_pos_x(), get_pos_y()))
			move(East)

		return result

	result = do_all(test)

	for row in result:
		quick_print(row)
