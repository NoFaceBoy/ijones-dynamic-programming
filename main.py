def get_number_of_paths(corridor: list, rows: int, columns: int):
    pass


with open("ijones1.in", "r") as input_file:
    in_data = input_file.readlines()
    row, column = map(int, in_data[0].split(' '))
    corridor = [in_data[line].rstrip('\n') for line in range(1, column + 1)]

open("ijones.out", "w").write(str(get_number_of_paths(corridor, row, column)))
