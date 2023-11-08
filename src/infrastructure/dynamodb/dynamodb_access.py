class DynamoDB:
    def __init__(self):
        self.table = {
            "U001": {
                "team_id": "U001",
                "team_name": "satake hirohumi",
                "rank": "1",
                "target_member_dict": {
                    "1": {
                        "name": "satake tarou",
                        "birth": "19940101",
                        "expiry_date": "20120401"
                    },
                    "2": {
                        "name": "satake jirou",
                        "birth": "19940101",
                        "expiry_date": "20130401"
                    },
                    "3": {
                        "name": "satake saburou",
                        "birth": "19950101",
                        "expiry_date": "20140401"
                    },
                    "4": {
                        "name": "satake shirou",
                        "birth": "19960101",
                        "expiry_date": "20150401"
                    },
                },
                "rec_expiry_date": "20150401"
            }
        }
    
    def get_item(self, Key: dict) -> dict:
        key_value = Key["team_id"]
        return self.table[key_value]

    def put_item(self, item: dict):
        key_value = item["team_id"]
        item_dict = {
            key_value: item
        }
        self.table = item_dict