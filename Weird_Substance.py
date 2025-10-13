def is_even(x,y):	
	
	return (x + y) % 2 == 0

while True:

	for i in range(get_world_size()):
		for j in range(get_world_size()):
			move(North)
			
			x,y = get_pos_x(), get_pos_y()	
			
			if can_harvest():	
				harvest()
				
			if is_even(x,y):		
				if get_water() < 0.7:
					use_item(Items.Water)
						
				plant(Entities.tree)
				use_item(Items.Weird_Substance)
				
			else:		
				plant(Entities.Bush)			
				
		move(East)
					