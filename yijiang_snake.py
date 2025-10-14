def maximize_dinosaur_bones():
    change_hat(Hats.Dinosaur_Hat)
    world_size = get_world_size()
    visited = set()

    while True:
        # 获取下一个苹果位置
        next_pos = measure()
        if not next_pos:
            continue

        target_x, target_y = next_pos

        # 螺旋式路径搜索
        while (get_pos_x(), get_pos_y()) != (target_x, target_y):
            # 优先横向移动
            if get_pos_x() < target_x and can_move(East):
                move(East)
            elif get_pos_x() > target_x and can_move(West):
                move(West)
            # 其次纵向移动
            elif get_pos_y() < target_y and can_move(North):
                move(North)
            elif get_pos_y() > target_y and can_move(South):
                move(South)
            else:
                # 路径阻塞时随机移动
                for dir in [North, East, South, West]:
                    if can_move(dir):
                        move(dir)
                        break
                    else:
                        # 无法移动时结束
                        change_hat(Hats.Straw_Hat)
                        return

        # 吃掉苹果后检查是否填满
        if len(visited) >= world_size**2 - 1:  # -1 排除起始位置
            change_hat(Hats.Straw_Hat)
            return

        visited.add((get_pos_x(), get_pos_y()))


if __name__ == "__main__":
    clear()
    maximize_dinosaur_bones()