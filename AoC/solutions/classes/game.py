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


class Cubes:
    def __init__(self, red, blue, green):
        self.red = red
        self.blue = blue
        self.green = green

    def is_subset_possible(self, red, blue, green):
        return self.red <= red and self.blue <= blue and self.green <= green