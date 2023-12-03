class Game:
    def __init__(self, id, cubes):
        self.id = id
        self.cubes = cubes

    def is_possible(self, red, blue, green):
        for subset in self.cubes:
            cubes = Cubes(subset.red, subset.blue, subset.green)
            if not cubes.is_subset_possible(red, blue, green):
                return False
        return True
    
    def minimal_amount_power(self):
        min_red = 0
        min_blue = 0
        min_green = 0
        for subset in self.cubes:
            cubes = Cubes(subset.red, subset.blue, subset.green)
            if cubes.red > min_red: min_red = cubes.red
            if cubes.blue > min_blue: min_blue = cubes.blue
            if cubes.green > min_green: min_green = cubes.green
        return min_red * min_blue * min_green

class Cubes:
    def __init__(self, red, blue, green):
        self.red = red
        self.blue = blue
        self.green = green

    def is_subset_possible(self, red, blue, green):
        return self.red <= red and self.blue <= blue and self.green <= green