# Import necessary modules (e.g., datetime for time tracking)
import datetime

# Create classes for Customers and Games
class Customer:
    def _init_(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance
        self.played_games = []

    def add_balance(self, amount):
        self.balance += amount

class Game:
    def _init_(self, title, price_per_hour, available_copies):
        self.title = title
        self.price_per_hour = price_per_hour
        self.available_copies = available_copies

# Create a class for the Gaming Cafe
class GamingCafe:
    def _init_(self):
        self.customers = []
        self.games = []
        self.active_sessions = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_game(self, game):
        self.games.append(game)

    def list_games(self):
        for game in self.games:
            print(f"{game.title} - ${game.price_per_hour}/hour ({game.available_copies} copies available)")

    def start_session(self, customer, game, hours):
        if customer in self.customers and game in self.games:
            if game.available_copies > 0:
                if customer.balance >= game.price_per_hour * hours:
                    if not any(session[0] == customer and session[1] == game for session in self.active_sessions):
                        game.available_copies -= 1
                        session_start_time = datetime.datetime.now()
                        self.active_sessions.append((customer, game, session_start_time, hours))
                        print(f"{customer.name} started playing {game.title} for {hours} hours.")
                    else:
                        print(f"{customer.name} is already in a session for {game.title}.")
                else:
                    print("Insufficient balance to start the session.")
            else:
                print(f"No available copies of {game.title} at the moment.")
        else:
            print("Customer or game not found.")

    def end_session(self, customer):
        for session in self.active_sessions:
            if session[0] == customer:
                game = session[1]
                session_start_time = session[2]
                hours_played = session[3]
                session_end_time = datetime.datetime.now()
                cost = game.price_per_hour * hours_played
                if session_end_time - session_start_time < datetime.timedelta(hours=hours_played):
                    # Calculate the remaining time and refund the balance
                    remaining_hours = (session_end_time - session_start_time).seconds / 3600
                    refund = game.price_per_hour * (hours_played - remaining_hours)
                    customer.balance += refund
                customer.balance -= cost
                game.available_copies += 1
                self.active_sessions.remove(session)
                print(f"{customer.name} ended the session for {game.title}.")
                print(f"Played for {hours_played} hours. Total cost: ${cost}.")
                print(f"Session started at {session_start_time} and ended at {session_end_time}.")
                break
        else:
            print(f"{customer.name} is not in an active session.")

# Example usage
if _name_ == "_main_":
    cafe = GamingCafe()

    customer1 = Customer("John", 18, 50)
    customer2 = Customer("Alice", 20, 40)

    game1 = Game("Fortnite", 5, 3)
    game2 = Game("League of Legends", 6, 2)

    cafe.add_customer(customer1)
    cafe.add_customer(customer2)
    cafe.add_game(game1)
    cafe.add_game(game2)

    cafe.list_games()

    cafe.start_session(customer1, game1, 2)
    cafe.start_session(customer2, game2, 3)
    cafe.end_session(customer1)