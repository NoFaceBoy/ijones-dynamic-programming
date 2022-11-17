def get_total_number_of_paths(corridor: list, width: int, height: int):
    total_paths = 0

    if height != 1:
        total_paths += get_paths(corridor, height - 1, width - 1)
        total_paths += get_paths(corridor, 0, width - 1)
    else:
        total_paths += get_paths(corridor, 0, width - 1)

    return total_paths


def get_paths(corridor: list, row: int, column: int):
    dp = [[0 for i in range(corridor_width)] for j in range(corridor_height)]
    path_sum = 0
    dp[row][column] = 1
    for column in range(corridor_width - 1, -1, -1):
        for row in range(corridor_height - 1, -1, -1):
            if dp[row][column]:
                possible_paths = dp[row][column]
            else:
                possible_paths = 0
                if column != corridor_width - 1:
                    for i in range(corridor_height - 1, -1, -1):
                        for j in range(corridor_width - 1, column, -1):
                            if corridor[i][j] == corridor[row][column] or (i == row and j == column + 1):
                                possible_paths += dp[i][j]
            dp[row][column] = possible_paths
    for i in range(corridor_height):
        path_sum += dp[i][0]

    return path_sum


with open("ijones1.in", "r") as import_file:
    lines = import_file.readlines()
    corridor_plates = [list(line.strip('\n')) for line in lines[1:]]
    corridor_width, corridor_height = map(int, lines[0].split(' '))

with open("ijones.out", 'w') as export_file:
    export_file.write(str(get_total_number_of_paths(corridor_plates, corridor_width, corridor_height)))
