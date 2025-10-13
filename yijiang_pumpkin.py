def for_all(f):

    def row():
        for _ in range(get_world_size() - 1):
            f()
            move(East)
        f()

    for _ in range(get_world_size()):
        if not spawn_drone(row):
            row()
        move(North)


def move_to(x, y):
    current_x, current_y = get_pos_x(), get_pos_y()
    size = get_world_size()
    
    # X轴最短路径计算
    dx = (x - current_x) % size
    if dx > size//2:
        move_dir_x = West
        steps_x = size - dx
    else:
        move_dir_x = East
        steps_x = dx
    
    # Y轴最短路径计算
    dy = (y - current_y) % size
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



def get_size():
    # 无人机数量和世界大小的较小值
    return min(get_world_size(), max_drones)


def pumpkin_row():
    for _ in range(get_world_size() - 1):
        plant(Entities.Pumpkin)
        move(East)
    plant(Entities.Pumpkin)


if __name__ == "__main__":
    clear()
    

    spawn_drone(pumpkin_row)
    move_to(15, 15)
           

