#OOPS
class ChessTournamentSystem:
    def __init__(self):
      self.players={}

    def add_player(self,player_id:str,name:str,rating:int)->dict:
        if player_id in self.players:
            raise ValueError('Player already exists')
        self.players[player_id]={
            'name':name,
            'rating':rating,
            'status':'Active'
        }

        return self.players

    def update_rating(self,player_id:str,new_rating:int)->dict:
        if player_id not in self.players:
            raise KeyError('Player not found')
        self.players[player_id]['rating']=new_rating

        return self.players

    def get_player_details(self,player_id:str)->dict:
        if player_id not in self.players:
            raise KeyError('Player not found')
        return self.players[player_id]

    def qualified_players(self,minimum_rating:int)->list:
        q_players=[]
        for k,v in self.players.items():
            if v['rating']>= minimum_rating:
                q_players.append(k)

        return q_players


# Create object
chess = ChessTournamentSystem()

# ==========================================
# TC1: ADD PLAYER
# ==========================================
print("===== TC1: ADD PLAYER =====")

print(chess.add_player("P101", "Arjun", 1850))

print(chess.add_player("P102", "Riya", 1700))

print(chess.add_player("P103", "Karthik", 2100))


# ==========================================
# TC2: UPDATE RATING
# ==========================================
print("\n===== TC2: UPDATE RATING =====")

print(chess.update_rating("P101", 1920))


# ==========================================
# TC3: GET PLAYER DETAILS
# ==========================================
print("\n===== TC3: GET PLAYER DETAILS =====")

print(chess.get_player_details("P101"))


# ==========================================
# TC4: QUALIFIED PLAYERS
# ==========================================
print("\n===== TC4: QUALIFIED PLAYERS =====")

print(chess.qualified_players(1800))


# ==========================================
# TC5: ERROR HANDLING
# ==========================================
print("\n===== TC5: ERROR HANDLING =====")

# Duplicate player
try:
    chess.add_player("P101", "Rahul", 1600)
except ValueError as e:
    print("Duplicate Error:", e)

# Update missing player
try:
    chess.update_rating("P999", 2000)
except KeyError as e:
    print("Missing Player Error:", e)

# Get missing player
try:
    chess.get_player_details("P999")
except KeyError as e:
    print("Missing Player Error:", e)

      
