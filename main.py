from sources import read_maze_from_file, find_min_way, beautiful_output


if __name__ == '__main__':
    maze = read_maze_from_file()
    min_way_length = find_min_way(maze, (0, 0), (4, 5))

    if min_way_length != -1:
        print(f'Длина минимального пути: {min_way_length}.')
        beautiful_output(maze)
    else:
        print('-1: Лабиринт непроходим')
