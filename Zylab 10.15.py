#Taylor Howard
#11-01-2020
#CIS2348-14654
#Zylab 10.15

class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def set_team_name(self, team_name):
            self.team_name = team_name

    def set_team_wins(self, team_wins):
            self.team_wins = team_wins

    def set_team_losses(self, team_losses):
            self.team_losses = team_losses

    # you have to write this percentage method
    def get_win_percentage(self):
        # calculate the percentage
        percentage = self.team_wins / (self.team_wins + self.team_losses)

        # return the answer
        return percentage
# main
if __name__ == '__main__':
    team = Team()
    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team.team_name = team_name
    team.team_wins = team_wins
    team.team_losses = team_losses

    # print the data
    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.team_name, 'has a winning average!')
    else:
        print('Team', team.team_name, 'has a losing average.')
