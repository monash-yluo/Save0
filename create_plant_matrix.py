plant_matrix = []


for y in range(get_world_size()):
	row_list = []

	for x in range(get_world_size()):

		if y >= get_world_size() // 2:
			if x >= get_world_size() // 2:
				row_list.append(Entities.Pumpkin)
			else:
				row_list.append(Entities.Carrot)

		else:
			if (x + y) % 2 == 0:
				row_list.append(Entities.Tree)
			else:
				row_list.append(Entities.Grass)

	plant_matrix.append(row_list)

print(plant_matrix)