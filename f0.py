import create_plant_matrix

def harvest_plant(plant_entity, use_water=False, water_below=0.7, use_fertilizer=False):

	# 洒水逻辑：当启用浇水且当前水位低于阈值时
	if use_water and get_water() < water_below:
		use_item(Items.Water)

	# 收获成熟作物
	if can_harvest():
		harvest()

	# 作物类型不匹配时重新种植
	if get_entity_type() != plant_entity:
		# 胡萝卜和南瓜需要松土条件
		if plant_entity in (Entities.Carrot, Entities.Pumpkin):
			# 检查当前地块是否为可种植的土壤
			if get_ground_type() != Grounds.Soil:
				till()  # 松土操作
		
		# 种植目标作物
		plant(plant_entity)


if __name__ == "__main__":
	clear()  # 初始化环境

	# 主循环：持续遍历整个农场
	while True:
		# 遍历Y轴坐标
		for y in range(get_world_size()):
			# 遍历X轴坐标
			for x in range(get_world_size()):
				# 从植物矩阵获取当前坐标应种植的作物类型
				plant_entity = create_plant_matrix.plant_matrix[y][x]
				
				# 执行收获/种植操作（启用自动浇水）
				harvest_plant(plant_entity, True)
				
				move(East)  # 向东移动一格
			
			move(North)  # 每行结束后向北移动换行

