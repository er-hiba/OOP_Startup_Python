class Player():
    def __init__(self, name, age, rank):
        self.name = name
        self.age = age
        self.rank = rank

    def info(self):
        print(f"Player: {self.name} \nAge: {self.age} \nRank: {self.rank}")

player1 = Player("Neymar Jr", 31, 13)

player2 = Player("Lionel Messi", 36, 4)

player2.info()
