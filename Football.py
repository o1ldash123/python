
class footBall :
   def __init__(self ,team , player) :
     self.team = team
     self.player = player


team1 = footBall("Real Madrid" , 11)
team2 = footBall("Barcelona" , 10)
team3 = footBall("Manchester United" , 7)


print('Team :' ,team1.team  , '\nPlayer :' ,team1.player )
print('Players :' ,team2.player , '\nTeam  :' ,team2.team )