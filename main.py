if __name__ == "__main__":
	clear()

	while (True):
		for y in range(get_world_size()):
			for x in range(get_world_size()):

				if can_harvest():

					harvest()
	
					if (y >= get_world_size() // 2 and False):

						if (get_ground_type() != Grounds.Soil):
							till()

						# print(get_water())
						if (get_water() < 0.7):
							use_item(Items.Water)

						plant(Entities.Carrot)

					else:
						if (x + y) % 2 == 0:

							if (get_water() < 0.7):
								use_item(Items.Water)

							plant(Entities.Tree)
	
				move(East)

			move(North)
