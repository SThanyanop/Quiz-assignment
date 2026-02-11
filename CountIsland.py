def CountIsland(map):
    found = 0

    rows = len(map)
    cols = len(map[0])

    seen = [[0 for x in range(cols)] for y in range(rows)]

    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(rows):
        for j in range(cols):
            if map[i][j] and not seen[i][j]:
                seen[i][j] = 1
                found += 1
                stack = [(i, j)]
                while len(stack):
                    x, y = stack.pop()
                    for sub_dir in dir:
                        if (
                            x + sub_dir[0] >= 0
                            and x + sub_dir[0] < rows
                            and y + sub_dir[1] >= 0
                            and y + sub_dir[1] < cols
                            and seen[x + sub_dir[0]][y + sub_dir[1]] == 0
                            and map[x + sub_dir[0]][y + sub_dir[1]]
                        ):
                            seen[x + sub_dir[0]][y + sub_dir[1]] += 1
                            stack.append((x + sub_dir[0], y + sub_dir[1]))
            seen[i][j] = 1

    return found


map = [[1, 0, 0, 1], [0, 1, 1, 1], [0, 0, 0, 1], [0, 1, 0, 1]]

print(CountIsland(map))
