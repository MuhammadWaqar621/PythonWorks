class Team: 
    #constructor which will initialize all required variable 
    def __init__(self, team_name, number_of_players, total_match, total_points): 
        self.team_name = team_name 
        self.number_of_players = number_of_players; 
        self.total_match = total_match 
        self.total_points = total_points
#this method will display the matches played by teams and their respective scores 
    def display_info(self):
        print("Team : {0}\t Matches Played: {1}\t Score: {2}".format(self.team_name, self.total_match, self.total_points))
        
 #creating 5 teams object 
team1 = Team("Milan", 16, 24, 30) 
team2 = Team("Manchester", 30, 120, 200) 
team3 = Team("Bercilona", 20, 200, 190) 
team4 = Team("Rial", 25, 90, 140) 
team5 = Team("Uventus", 22, 80, 100)
#displaying all team info 
team1.display_info() 
team2.display_info() 
team3.display_info() 
team4.display_info() 
team5.display_info()
