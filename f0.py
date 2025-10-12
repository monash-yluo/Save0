import create_plant_matrix

def harvest_plant(plant_entity, use_water=False, water_below=0.7, use_fertilizer=False):

	# 洒水
	if use_water and get_water() < water_below:
		use_item(Items.Water)

	# 收获
	if can_harvest():
		harvest()

	if get_entity_type() != plant_entity:
		# 松土
		if(plant_entity == Entities.Carrot or plant_entity == Entities.Pumpkin):
			if get_ground_type() != Grounds.Soil:
				till()
			
		# 种植
		plant(plant_entity)


if __name__ == "__main__":
	clear()

	while True:
		for y in range(get_world_size()):
			for x in range(get_world_size()):

				plant_entity = create_plant_matrix.plant_matrix[y][x]

				harvest_plant(plant_entity, True)

				move(East)

			move(North)
