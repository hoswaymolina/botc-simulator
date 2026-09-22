import sqlite3

from game import *
from data import *

def simulate_games(n):
    master_game_log = []
    for i in range(1, n+1):
        game = Game(assign_roles(), i, [])
        run_game(game)
        master_game_log.append(game.game_log)

    games = []
    events = []
    for log in master_game_log:
        for event in log:
            if event.event_type == EventType.GAME_END:
                games.append(event)
            else:
                events.append(event)

    return games, events