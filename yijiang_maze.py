def creat_maze():
    plant(Entities.Bush)
    substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)


def dfs_solve_maze():
    start_x, start_y = get_pos_x(), get_pos_y()

    stack = [(start_x, start_y, None)]  # (x, y, 到达此位置的方向)
    visited = set()
    visited.add((start_x, start_y))
    path = [(start_x, start_y, None)]  # 实际移动的路径

    while stack:

        x, y, move_dir = stack.pop()
        # quick_print(visited, stack, x, y, move_dir)

        # 执行移动（如果是第一次访问该位置）
        if move_dir:
            move(move_dir)
            path.append((get_pos_x(), get_pos_y(), move_dir))
            visited.add((get_pos_x(), get_pos_y()))

        # 检查是否到达终点
        if get_entity_type() == Entities.Treasure:
            return True

        # 尝试所有可能的方向
        found_move = False
        for direction in [North, South, East, West]:
            if can_move(direction):
                # 计算新位置
                new_x, new_y = get_pos_x(), get_pos_y()
                if direction == North:
                    new_y += 1
                elif direction == South:
                    new_y -= 1
                elif direction == East:
                    new_x += 1
                elif direction == West:
                    new_x -= 1

                if (new_x, new_y) not in visited:
                    stack.append((get_pos_x(), get_pos_y(), direction))
                    found_move = True

        # 如果没有找到可移动的方向，回溯
        if not found_move and path:
            # 移除直到和stack中下一个的起始位置一样
            while path and (get_pos_x(), get_pos_y()) != (stack[-1][0], stack[-1][1]):
                last_path = path.pop()
                move(get_opposite_dir(last_path[2]))

    return False


def get_opposite_dir(dir):
    if dir == North:
        return South
    elif dir == South:
        return North
    elif dir == East:
        return West
    elif dir == West:
        return East
    return None

def main_299_challenge():
    clear()
    plant(Entities.Bush)

    for i in range(299):
        substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
        use_item(Items.Weird_Substance, substance)
        dfs_solve_maze()

    harvest()

def main():
    clear()
    while True:
        creat_maze()
        dfs_solve_maze()
        harvest()

if __name__ == "__main__":
    main_299_challenge()
