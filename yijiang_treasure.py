from yijiang_companion import *



if __name__ == "__main__":
	clear()  # 初始化环境

	for i in range(max_drones() - 1):
		def treasure_1x1():
			# 移动到 treasure 位置
			move_to(i % get_world_size(), i // get_world_size())

			for _ in range(3000):
				pass

			while True:
				plant(Entities.Bush)
				use_item(Items.Weird_Substance, 1)

				harvest()

		spawn_drone(treasure_1x1)

	i += 1
	treasure_1x1()
	
