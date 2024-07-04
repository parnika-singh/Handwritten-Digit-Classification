class Aquarium:
    def __init__(self, length, width, height, water_type):
        self.length = length
        self.width = width
        self.height = height
        self.water_type = water_type
        self.fish = []

    def add_fish(self, fish_name):
        self.fish.append(fish_name)

    def print_details(self):
        print(f"Aquarium dimensions: {self.length} x {self.width} x {self.height}")
        print(f"Water type: {self.water_type}")
        if self.fish:
            print("Fish in the aquarium:")
            for fish in self.fish:
                print(f"- {fish}")
        else:
            print("No fish in the aquarium.")

# Example usage
my_aquarium = Aquarium(100, 50, 60, 'Freshwater')
my_aquarium.add_fish('Goldfish')
my_aquarium.add_fish('Angelfish')
my_aquarium.print_details()
