class Team:
    def __init__(self, team_id:str, team_name:str, rank:str, target_member_dict:list, rec_expiry_date:str):
        if len(target_member_dict) > 5:
            self.team_id = team_id
            self.team_name = team_name
            self.target_member_dict = target_member_dict
            self.rank = rank
        else:
            raise Exception("team member count over")