while(True):
	clear()
	
	list = []
	
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			
			if get_entity_type() == Entities.Grass:
				till()
			plant(Entities.Sunflower)					
			list.append(measure())		
			
			move(East)
		move(North) 
	
	max_index = 0
	max_index_befor = 0
	max_flowers = 0
	
	for i in range(30000):
		pass
	for i in range(len(list)):

		a = get_pos_x()
		b = get_pos_y() 
		for index in range(len(list)):
			if list[index] > list[max_index]:
				max_index = index
		x = (max_index) % get_world_size()
		y = (max_index) // get_world_size()
		quick_print(x,y)
			
		if x-a >= 0:
			for i in range(x-a):
				move(East)
		if x-a < 0:
			for i in range(a-x):
				move(West)	
		if y-b >= 0:
			for i in range(y-b):
				move(North)
		if y-b < 0:
			for i in range(b-y):
				move(South)
						
		if can_harvest():
			harvest()
			list.pop(max_index)
			list.insert(max_index,0)
			
			#种植向日葵，没删列，未生效，懒得改，改了也没用
			if len(list) <= 10:
				list.pop(max_index)
				plant(Entities.Sunflower)
				list.insert(max_index,measure())
			
			if max_flowers != 0:
				list.pop(max_index_befor)
				list.insert(max_index_befor,max_flowers)
				max_flowers = 0
		else:
			max_index_befor = max_index
			max_flowers = list[max_index]
			list.pop(max_index)
			
			if max_flowers in list:
				list.insert(max_index,0)
				
			else:
				list.insert(max_index,max_flowers)
				max_flowers = 0


				
				
				