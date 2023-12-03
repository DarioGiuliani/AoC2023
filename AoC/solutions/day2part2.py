from utils.file_reader import FileReader
from classes.game import Game,Cubes

input = FileReader.readfile("day2part2input.txt")
total = 0

for element in input:
    stripped_element = element.strip()
    split_game = stripped_element.split(":")
    game_id = int(split_game[0].split(" ")[1].strip())
    sub_sets = split_game[1].strip().split(";")
    collect_subsets = []
    for set in sub_sets:
        set_split = set.strip().split(",")
        green = 0
        red = 0
        blue = 0
        for set_element in set_split:
            if "green" in set_element:
                green = int(set_element.strip().split(" ")[0].strip())
            if "red" in set_element:
                red = int(set_element.strip().split(" ")[0].strip())
            if "blue" in set_element:
                blue = int(set_element.strip().split(" ")[0].strip())
        collect_subsets.append(Cubes(red, blue, green))
    game = Game(game_id, collect_subsets)
    total += game.minimal_amount_power()
print(total)