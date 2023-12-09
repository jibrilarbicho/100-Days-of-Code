class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Exhale", "Inhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("move in water")


memo = Fish()
memo.swim()
memo.breathe()
print(memo.num_eyes)
