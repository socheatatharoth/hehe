class SportLeague:
    
    def __init__(self):
        self.team = {}

    def add_team(self, team_name):
        if team_name not in self.team:
            self.team[team_name] = []
            return f"Team {team_name} added."
        return f"Team {team_name} already exists."
    
    def add_player(self, team_name, id_player, name, position):
        if team_name not in self.team:
            return f"Team {team_name} does not exist. Please add the team first."
        
        if any(player['ID'] == id_player for player in self.team[team_name]):
            return f"Player with ID {id_player} already exists in team {team_name}."
        
        new_player = {"ID": id_player, "Name": name, "Position": position}
        self.team[team_name].append(new_player)
        return f"Player {name} added to team {team_name}"
    
    def view_team(self, team_name):
        if team_name in self.team:
            players = "\n".join(
                f"ID: {player['ID']}, Name: {player['Name']}, Position: {player['Position']}"
                for player in self.team[team_name]
            )
            return f"Team {team_name} players:\n{players}" if players else f"Team {team_name} has no players."
        return f"Team {team_name} not found."
    
    def update_player(self, team_name, id_player, name=None, position=None):
        if team_name in self.team:
            for player in self.team[team_name]:
                if player['ID'] == id_player:
                    if name is not None:
                        player['Name'] = name  
                    if position is not None:
                        player['Position'] = position  
                    return f"Player {id_player} updated in team {team_name}."
            return f"Player with ID {id_player} not found in team {team_name}."
        return f"Team {team_name} does not exist."

    def remove_player(self, team_name, id_player):
        if team_name not in self.team:
            return f"Team {team_name} does not exist."
        
        for index, player in enumerate(self.team[team_name]):
            if player['ID'] == id_player:
                removed_player = self.team[team_name].pop(index)
                return f"Player {removed_player['Name']} removed from team {team_name}."
        
        return f"Player with ID {id_player} not found in team {team_name}."

# Testing the updated code
sportleague = SportLeague()

print(sportleague.add_team("Tiger"))
print(sportleague.add_player("Tiger", 1, "Serey", "Goalkeeper"))
print(sportleague.add_player("Tiger", 2, "Dy", "Goalkeeper"))

print(sportleague.add_team("Lion"))
print(sportleague.add_player("Lion", 1, "Dara", "Striker"))
print(sportleague.add_player("Lion", 2, "Ly", "Defender"))

print(sportleague.update_player("Tiger", 1, "Serey", "Goalkeeper"))

print(sportleague.view_team("Tiger"))
print(sportleague.remove_player("Tiger", 2))  
print(sportleague.view_team("Tiger"))
