class Customer:
    def _init_(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

class Game:
    def _init_(self, title, price_per_hour):
        self.title = title
        self.price_per_hour = price_per_hour

class GamingCafe:
    def _init_(self):
        self.customers = []
        self.games = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_game(self, game):
        self.games.append(game)

    def list_games(self):
        for game in self.games:
            print(f"{game.title} - ${game.price_per_hour}/hour")

    def play_game(self, customer, game, hours):
        if customer in self.customers and game in self.games:
            cost = game.price_per_hour * hours
            if customer.balance >= cost:
                customer.balance -= cost
                print(f"{customer.name} played {game.title} for {hours} hours. Total cost: ${cost}")
            else:
                print(f"Insufficient balance for {customer.name} to play {game.title}.")
        else:
            print("Customer or game not found.")

if _game_ == "_main_":
    cafe = GamingCafe()

    customer1 = Customer("John", 18, 50)
    customer2 = Customer("Alice", 20, 40)

    game1 = Game("Fortnite", 5)
    game2 = Game("League of Legends", 6)

    cafe.add_customer(customer1)
    cafe.add_customer(customer2)
    cafe.add_game(game1)
    cafe.add_game(game2)

    cafe.list_games()

    cafe.play_game(customer1, game1, 2)
    cafe.play_game(customer2,game2,3)