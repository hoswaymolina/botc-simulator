import random
from math import ceil

from roles import *
from player import *
from assignment import *

class Game:
    """A class representing a Game, which acts as a storyteller by 
    managing information requests."""

    def __init__(self, players, game_id, game_log):
        self.players = players
        self.day = 1
        self.night = 1
        self.phase = "night"
        self.game_id = game_id
        self.game_log = game_log

    def alive_players(self):
        return [p for p in self.players if p.alive]

    def check_win(self):
        demon_check = False
        for p in self.alive_players():
            if isinstance(p.role, Demon):
                demon_check = True
                continue

        if not demon_check:
            game_over = Event(self.game_id, self.day, self.phase,
                              EventType.GAME_END, metadata={'winner': 'good'})
            self.game_log.append(game_over)
            print("Good wins")
            return True

        if len(self.alive_players()) <= 2:
            game_over = Event(self.game_id, self.day, self.phase,
                              EventType.GAME_END, metadata={'winner': 'evil'})
            self.game_log.append(game_over)
            print("Evil wins")
            return True

        return False

def night_phase(game):

    if game.night == 1:
        # "First Night"
        game.night += 1
        game.phase = "day"

    else:
        # "Other Nights"  
        
        for player in game.alive_players():
            if isinstance(player.role, Imp):
                targets = [p for p in game.alive_players()
                           if p.role.alignment == "good"]
                if not targets:
                    targets.extend([p for p in game.alive_players()
                                   if not isinstance(p, Demon)])
                target = random.choice(targets)
                player.role.use_ability(target)
                kill = Event(game.game_id, game.day, game.phase,
                             EventType.NIGHT_KILL, player.number, target.number)
                game.game_log.append(kill)

        game.night += 1
        game.phase = "day"

def day_phase(game):

    nominators = [p for p in game.alive_players()]
    for n in nominators:
        n.nomination_left = True

    execution_threshold = ceil(len(game.players)/2)
    on_the_block = None
    tally_to_beat = 0

    for n in nominators:
        if n.nomination_left:
            accused = random.choice(game.alive_players())
            n.nomination_left = False
            votes = 0
            for p in game.players:
                vote = random.choice([True, False])
                if vote:
                    votes += 1
            if votes >= execution_threshold:
                if on_the_block:
                    if votes < tally_to_beat:
                        pass
                    elif votes == tally_to_beat:
                        on_the_block = None
                        execution_threshold = tally_to_beat + 1
                    else:
                        on_the_block = accused
                        tally_to_beat = votes
                else:
                    on_the_block = accused
                    tally_to_beat = votes
            
    if on_the_block:
        execution = Event(game.game_id, game.day, game.phase,
                          EventType.EXECUTION, actor=None,
                          target=on_the_block.number)
        on_the_block.alive = False
        game.game_log.append(execution)

    game.day += 1
    game.phase = "night"

def run_game(game):
    while True:
        night_phase(game)
        if game.check_win():
            break
        day_phase(game)
        if game.check_win():
            break