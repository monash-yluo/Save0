from yijiang_tool import *
from yijiang_maze import *



def place_1():
	list = [(2,2),(2,7),(2,12),(2,17),(7,2),(7,7),(7,12),(7,17),(12,2),(12,7),(12,12),(12,17),(17,2),(17,7),(17,12)]
	move_to(list[i][0],list[i][1])
	for _ in range(6000):
		pass
	while True:
		plant(Entities.Bush)
		for _ in range(300):
			use_item(Items.Weird_Substance, 160)
			dfs_solve_maze()
		harvest()
		move_to(list[i][0],list[i][1])
	
	
def place_2():
	list = [(3,23),(3,29),(9,23),(9,29),(15,23),(15,29),(23,3),(29,3),(23,9),(29,9),(23,15),(29,15)]
	move_to(list[i][0],list[i][1])
	for _ in range(6000):
		pass
	while True:
		plant(Entities.Bush)
		for _ in range(300):
			use_item(Items.Weird_Substance, 192)
			dfs_solve_maze()
		harvest()
		move_to(list[i][0],list[i][1])

def place_3():
	list = [(28,28),(28,21),(21,28),(21,21)]
	move_to(list[i][0],list[i][1])
	for _ in range(6000):
		pass
	while True:
		plant(Entities.Bush)
		for _ in range(300):
			use_item(Items.Weird_Substance, 224)
			dfs_solve_maze()
		harvest()
		move_to(list[i][0],list[i][1])
			
			
if __name__ == '__main__':	
	harvest()
	while True:
		clear()
		for i in range(15):
			spawn_drone(place_1)
		for i in range(12):
			spawn_drone(place_2)
		for i in range(4):
			spawn_drone(place_3)
		move_to(16,16)
		for i in range(6000):
			pass
		while True:
			plant(Entities.Bush)
			for _ in range(300):
				use_item(Items.Weird_Substance, 96)
				dfs_solve_maze()
			harvest()
			move_to(16,16)
	