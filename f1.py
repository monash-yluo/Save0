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

def location():
		location = (get_pos_x(),get_pos_y())
		return location
		
if wait_for(spawn_drone(location)) == (get_pos_x(),get_pos_y()): 
		if random() < 0.5:
			move(North)