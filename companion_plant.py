def move_to(x,y):
	#移动
	a = get_pos_x()
	b = get_pos_y()
	size = get_world_size()
	dx = (x - a) % size
	if dx > size//2:
		move_dir_x = West
		steps_x = size - dx
	else:
		move_dir_x = East
		steps_x = dx
		
	# Y轴最短路径计算
	dy = (y - b) % size
	if dy > size//2:
		move_dir_y = South
		steps_y = size - dy
	else:
		move_dir_y = North
		steps_y = dy
		
	# 执行移动
	for _ in range(steps_x):
		move(move_dir_x)
	for _ in range(steps_y):
		move(move_dir_y)


		
def drone_plant():
	
	move(mun)
	move(mun)
	move(mun)
	move(mun)
	
	list = []
	
	for _ in range(4):
					
		if get_companion() == None:
			plant(Entities.Carrot)
			plant_type, (x, y) = get_companion()
			
		else:
			plant_type, (x, y) = get_companion()
			
		move_to(x,y)
		list.append((x,y))
		
		if get_water() < 0.7:
			use_item(Items.Water)
	
		if get_entity_type() != plant_type:
			if plant_type in (Entities.Carrot,Entities.Tree):
				if get_ground_type() != Grounds.Soil:
					till()
						
		if can_harvest():
			harvest()
				
		plant(plant_type)
		
	for i in range(len(list)): 
		move_to(list[i][0],list[i][1])
		if can_harvest():
			harvest()


if __name__ == "__main__":
	clear()
	while True:
		for y in range(get_world_size()):
			for x in range(get_world_size()):
				for mun in [East, West, North, South]:
					spawn_drone(drone_plant)
				move(East)
				move(East)
				move(East)
				move(East)
			
			move(North)
			move(North)
			move(North)
			move(North)


	