import database_connections
import random

db = database_connections.Database("codenames.db")

base = (['R'] * 8) + (['B'] * 8) + (['C'] * 7) + ['A']
templates = []
for _ in range(50):
    starting = 'R' if random.choice([True, False]) else 'B'
    cards = base + [starting]
    random.shuffle(cards)
    db.add_board_layout(starting, "".join(cards))
