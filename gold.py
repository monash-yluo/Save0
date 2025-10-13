def harvest_column():
	move(i)
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, 1)
	harvest()
	
clear()		
move(East)
move(North)
while (True):
	list = [East, West, North, South]
	for i in list:
		spawn_drone(harvest_column)


	