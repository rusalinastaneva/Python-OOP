from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.players = []

    def add(self, player: Player):
        if any(p.username == player.username for p in self.players):
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)

    @property
    def count(self):
        return len(self.players)

    def remove(self, player_name: str):
        if player_name == "":
            raise ValueError("Player cannot be an empty string!")
        found_player = self.find(player_name)
        self.players.remove(found_player)

    def find(self, username: str):
        found_player = [player for player in self.players if player.username == username][0]
        return found_player
