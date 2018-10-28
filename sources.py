from queue import PriorityQueue
from textwrap import wrap
from copy import deepcopy
from colorama import init, Fore, Style


def read_maze_from_file():
    with open('maze.txt', 'r', encoding='utf-8') as f:
        maze = [wrap(row, 1) for row in f if row != '\n']

    if len(set(len(row) for row in maze)) != 1:
        raise ValueError('All rows must have the same length')

    return maze


def check_permeability(lab, pos):
    if pos == (len(lab) - 1, len(lab[0]) - 1):
        return True

    lab[pos[0]][pos[1]] = '1'

    if pos[0] < len(lab) - 1 and lab[pos[0] + 1][pos[1]] not in ('#', '1'):
        if check_permeability(lab, (pos[0] + 1, pos[1])):
            return True

    if pos[1] < len(lab[0]) - 1 and lab[pos[0]][pos[1] + 1] not in ('#', '1'):
        if check_permeability(lab, (pos[0], pos[1] + 1)):
            return True

    if pos[1] > 0 and lab[pos[0]][pos[1] - 1] not in ('#', '1'):
        if check_permeability(lab, (pos[0], pos[1] - 1)):
            return True

    if pos[0] > 0 and lab[pos[0] - 1][pos[1]] not in ('#', '1'):
        if check_permeability(lab, (pos[0] - 1, pos[1])):
            return True

    return False


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def find_min_way(lab, start, goal):

    if lab[start[0]][start[1]] == '#' \
            or not check_permeability(deepcopy(lab), (0, 0)):
        return -1

    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}
    way_length = 0

    while not frontier.empty():
        curr = frontier.get()

        if curr == goal:
            while curr != start:
                lab[curr[0]][curr[1]] = '*'
                curr = came_from[curr]
                way_length += 1
            lab[start[0]][start[1]] = '*'
            return way_length

        for next in [(curr[0] + 1, curr[1]), (curr[0], curr[1] + 1),
                     (curr[0], curr[1] - 1), (curr[0] - 1, curr[1])]:
            try:
                checker = lab[next[0]][next[1]] != '#'
            except IndexError:
                continue

            new_cost = cost_so_far[curr] + 1

            if checker and (next not in cost_so_far or new_cost < cost_so_far[next]):
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = curr


def beautiful_output(lab):
    init()

    for row in lab:
        if '*' not in row:
            print(*row)
            continue

        for sym in row:
            if sym != '*':
                print(sym, end=' ')
                continue
            print(Fore.GREEN + sym, end=' ')
            print(Style.RESET_ALL, end='')

        print()
