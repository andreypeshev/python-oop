from project2.player import Player

class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player not in self.players:
            if player.guild == 'Unaffiliated':
                self.players.append(player)
                player.guild = self.name
                return f"Welcome player {player.name} to the guild {self.name}"
            return f"Player {player.name} is in another guild."
        return f"Player {player.name} is already in the guild."

    def kick_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                player.guild = 'Unaffiliated'
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players_list = [player.player_info() for player in self.players]
        nl = "\n"

        return f"Guild: {self.name}\n" \
               f"{nl.join(players_list)}"


